import os
import json
import re
import hashlib
import sys
import argparse
from datetime import datetime

STATE_FILE = os.path.join(os.path.dirname(__file__), '../../../../.agent/translation_state.json')
SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../docs_zh'))
TARGET_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../docs'))
EXCLUSION_FILE = os.path.join(os.path.dirname(__file__), '../../../../.agent/exclusion.json')

def load_exclusion_list():
    try:
        if os.path.exists(EXCLUSION_FILE):
            with open(EXCLUSION_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Parse excludes as relative paths, assuming base_path context
                return [p.replace('\\', '/') for p in data.get('excludes', [])]
    except Exception as e:
        print(f"Warning: Failed to load exclusion list: {e}")
    return []

def load_state():
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                # Migration: If simple key-value (string hash), convert to object or clear
                # For safety/cleanliness as per user request to use new logic,
                # we will treat old string hashes as partial data or just clear them if invalid.
                # Actually, let's migrate: old hash was source hash.
                new_data = {}
                for k, v in data.items():
                    if isinstance(v, str):
                        new_data[k] = {"source_hash": v, "target_hash": None}
                    else:
                        new_data[k] = v
                return new_data
            except json.JSONDecodeError:
                return {}
    return {}

def save_state(state):
    # Ensure directory exists
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def get_file_hash(file_path):
    """Calculate MD5 hash of a file."""
    if not os.path.exists(file_path):
        return None
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_relative_path(abs_path, root):
    try:
        rel = os.path.relpath(abs_path, root)
        return rel.replace('\\', '/')
    except ValueError:
        return abs_path

def scan_files(root_dir):
    md_files = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def get_files_to_translate(target_path=None, force=False, show_all=False):
    """Returns a list of tuples: (source_path, target_path, reason)"""
    state = load_state()
    exclusion_list = load_exclusion_list()
    files_to_translate = []
    
    source_files = scan_files(SOURCE_ROOT)
    
    # Normalize target_path for prefix matching
    target_rel_prefix = None
    if target_path:
        try:
             if os.path.isabs(target_path):
                 target_rel_prefix = get_relative_path(target_path, SOURCE_ROOT)
             else:
                 target_rel_prefix = target_path # Assume relative
             target_rel_prefix = target_rel_prefix.replace('\\', '/')
        except:
             pass

    for source_path in source_files:
        rel_path = get_relative_path(source_path, SOURCE_ROOT)
        normalized_rel = rel_path.replace('\\', '/')
        target_path_abs = os.path.join(TARGET_ROOT, rel_path)
        
        # Check exclusion list
        is_excluded = False
        for exclude in exclusion_list:
            if normalized_rel == exclude or normalized_rel.startswith(exclude + '/'):
                is_excluded = True
                break
        
        if is_excluded:
            if show_all:
                files_to_translate.append({
                    "source": source_path,
                    "target": target_path_abs,
                    "relative": rel_path,
                    "current_hash": None,
                    "reason": "Ignored"
                })
            continue
        
        # Filter by path if provided
        if target_rel_prefix:
            if not (normalized_rel == target_rel_prefix or normalized_rel.startswith(target_rel_prefix + '/')):
                continue

        target_path_abs = os.path.join(TARGET_ROOT, rel_path)
        
        target_exists = os.path.exists(target_path_abs)
        current_source_hash = get_file_hash(source_path)
        current_target_hash = get_file_hash(target_path_abs) if target_exists else None
        
        record = state.get(rel_path)
        
        # New Sync Logic
        reason = None
        
        if force:
            reason = "Forced"
        elif record is None:
            # No record found
            if not target_exists:
                reason = "New"
            else:
                reason = "Untracked" # New + Target Exists
        else:
            # Record exists
            stored_source_hash = record.get("source_hash")
            stored_target_hash = record.get("target_hash")
            
            if not target_exists:
                reason = "Missing Target"
            elif stored_source_hash != current_source_hash:
                reason = "Source Modified"
            elif stored_target_hash != current_target_hash:
                reason = "Target Modified"
            elif show_all:
                reason = "Translated" # Synced
        
        if reason:
            files_to_translate.append({
                "source": source_path,
                "target": target_path_abs,
                "relative": rel_path,
                "current_hash": current_source_hash, # Keep for compatibility if needed
                "current_target_hash": current_target_hash,
                "reason": reason,
                "target_exists": target_exists
            })
            
    return files_to_translate

def mark_as_translated(rel_path, source_hash, target_hash=None):
    state = load_state()

    # If target_hash is not provided (legacy call tests?), calculate it from target file
    if target_hash is None:
        target_path_abs = os.path.join(TARGET_ROOT, rel_path)
        target_hash = get_file_hash(target_path_abs)

    # Normalize hashes to lowercase to avoid case-sensitive mismatch (e.g., PowerShell Get-FileHash -> uppercase)
    norm_source_hash = source_hash.lower() if isinstance(source_hash, str) else source_hash
    norm_target_hash = target_hash.lower() if isinstance(target_hash, str) else target_hash

    state[rel_path] = {
        "source_hash": norm_source_hash,
        "target_hash": norm_target_hash
    }
    save_state(state)
    print(f"Updated state for {rel_path}")



def clean_stale_records():
    state = load_state()
    keys_to_remove = []
    
    # Identify stale records
    for rel_path in state.keys():
        source_path = os.path.join(SOURCE_ROOT, rel_path)
        if not os.path.exists(source_path):
            keys_to_remove.append(rel_path)
            
    if not keys_to_remove:
        return

    # Process removal
    for rel_path in keys_to_remove:
        # Remove from state
        del state[rel_path]
        print(f"移除過時記錄: {rel_path}", file=sys.stderr)
        
        # Remove target file if exists
        target_path = os.path.join(TARGET_ROOT, rel_path)
        if os.path.exists(target_path):
            try:
                os.remove(target_path)
                print(f"已刪除孤立目標檔: {target_path}", file=sys.stderr)
            except Exception as e:
                print(f"刪除目標檔失敗 {target_path}: {e}", file=sys.stderr)
                
    save_state(state)

def process_exclusions_from_report(report_file):
    if not os.path.exists(report_file):
        print(f"錯誤: 找不到報告檔案 {report_file}")
        return

    exclusion_list = load_exclusion_list()
    new_exclusions = []
    
    with open(report_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Match Table rows starting with | [x] or | [X]
            if re.match(r'^\|\s*\[[xX]\]\s*\|', line):
                # Extract path from code block `path`
                match = re.search(r'`([^`]+)`', line)
                if match:
                    path = match.group(1)
                    if path not in exclusion_list and path not in new_exclusions:
                        new_exclusions.append(path)

    if new_exclusions:
        exclusion_list.extend(new_exclusions)
        
        # Sort and save
        exclusion_list.sort()
        
        # Preserve original structure if possible, but minimal valid JSON is fine
        output_data = {
            "base_path": "docs_zh",
            "excludes": exclusion_list
        }
        
        try:
            with open(EXCLUSION_FILE, 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=4, ensure_ascii=False)
            print(f"成功將 {len(new_exclusions)} 個檔案加入排除清單。")
            
            # Regenerate report to reflect changes
            generate_report(report_file)
            
        except Exception as e:
            print(f"儲存排除清單時發生錯誤: {e}")
    else:
        print("未發現任何勾選 [x] 的新增排除項目。")

def generate_report(output_file):
    # Ensure cleanup runs before report
    clean_stale_records()
    
    files = get_files_to_translate(show_all=True)
    
    # Sort files
    def sort_key(item):
        order = {
            "Source Modified": 0, 
            "Target Modified": 0, 
            "New": 1, 
            "Untracked": 1, 
            "Missing Target": 2, 
            "Translated": 4, 
            "Ignored": 5
        }
        return (order.get(item['reason'], 9), item['relative'])
        
    files.sort(key=sort_key)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 翻譯狀態報告\n\n")
        f.write(f"產生時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("> 💡 **提示**: 在「排除」欄位打勾 `[x]` (將 `[ ]` 改為 `[x]`)，然後執行指令即可自動將該檔案加入排除名單。\n\n")
        f.write("| 排除 | 狀態 | 說明 | 檔案路徑 | 備註 |\n")
        f.write("| :---: | :---: | :--- | :--- | :--- |\n")
        
        stats = {"Total": len(files), "Translated": 0, "Pending": 0, "Ignored": 0}
        
        # Format: (Icon, Text)
        status_map = {
            "New": ("🔴", "**新增**"),
            "Untracked": ("🔴", "**未追蹤**"), # Internal logic mapped below
            "Source Modified": ("🟡", "**來源已改**"),
            "Target Modified": ("🟣", "**目標已改**"),
            "Missing Target": ("🟠", "**遺失目標**"),
            "Translated": ("🟢", "**已翻譯**"),
            "Ignored": ("⚪", "**已忽略**")
        }
        
        for item in files:
            reason_key = item['reason']
            
            # Default to key if not found (shouldn't happen)
            val = status_map.get(reason_key, ("", reason_key))
            
            # Map Untracked to "New" icon/text but add remark
            if reason_key == "Untracked":
                val = status_map["New"]
            
            icon, text = val
            
            rel_path = item['relative']
            rel_path = rel_path.replace("|", "\\|")
            
            remark = ""
            if reason_key == "Untracked":
                remark = "⚠️ 目標檔已存在"
            
            links = f"[📄](docs_zh/{rel_path})"
            if item.get('target_exists', False):
                links += f" [🎯](docs/{rel_path})"
            
            f.write(f"| [ ] | {icon} | {text} | `{rel_path}` {links} | {remark} |\n")
            
            if reason_key == "Translated":
                stats["Translated"] += 1
            elif reason_key == "Ignored":
                stats["Ignored"] += 1
            else:
                stats["Pending"] += 1
                
        f.write(f"\n**摘要**: 總計 {stats['Total']} 個檔案。 {stats['Translated']} 個已翻譯， {stats['Pending']} 個待翻譯， {stats['Ignored']} 個已忽略。\n")
    
    print(f"報告已產生: {output_file}")

if __name__ == "__main__": 
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['scan', 'update', 'report', 'process_exclusions'], help='執行動作')
    parser.add_argument('--file', help='要更新的檔案相對路徑 (用於 update)', required=False)
    parser.add_argument('--hash', help='來源 Hash 值 (用於 update)', required=False)
    parser.add_argument('--target_hash', help='目標 Hash 值 (用於 update)', required=False)
    parser.add_argument('--path', help='指定掃描路徑 (檔案或目錄)', required=False)
    parser.add_argument('--force', action='store_true', help='強制包含所有檔案')
    parser.add_argument('--all', action='store_true', help='結果包含已翻譯檔案 (用於報告)')
    parser.add_argument('--output', help='報告輸出檔名', default='TRANSLATION_STATUS.md')
    
    args = parser.parse_args()
    
    if args.action == 'scan':
        clean_stale_records()
        to_translate = get_files_to_translate(args.path, args.force, args.all)
        # For JSON output, we might want to clean up the keys
        print(json.dumps(to_translate, indent=2, ensure_ascii=False))
        
    elif args.action == 'update':
        if not args.file or not args.hash:
            print("Error: --file and --hash are required for update action")
            sys.exit(1)
        # target_hash is optional in CLI but logic might need it. 
        # If not provided, mark_as_translated will try to calc it from file.
        mark_as_translated(args.file, args.hash, args.target_hash)
        
    elif args.action == 'report':
        generate_report(args.output)
        
    elif args.action == 'process_exclusions':
        process_exclusions_from_report(args.output)

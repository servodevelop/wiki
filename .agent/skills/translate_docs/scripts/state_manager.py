import os
import json
import hashlib
import sys

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
                return json.load(f)
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

def get_files_to_translate(target_path=None, force=False):
    """Returns a list of tuples: (source_path, target_path, reason)"""
    state = load_state()
    exclusion_list = load_exclusion_list()
    files_to_translate = []
    
    source_files = scan_files(SOURCE_ROOT)
    
    # Normalize target_path for prefix matching
    target_rel_prefix = None
    if target_path:
        # Convert absolute or relative input to relative path from SOURCE_ROOT
        # If input is absolute path to a file in docs_zh
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
        
        # Check exclusion list
        is_excluded = False
        for exclude in exclusion_list:
            if normalized_rel == exclude or normalized_rel.startswith(exclude + '/'):
                is_excluded = True
                break
        
        if is_excluded:
            continue
        
        # Filter by path if provided
        if target_rel_prefix:
            if not (normalized_rel == target_rel_prefix or normalized_rel.startswith(target_rel_prefix + '/')):
                continue

        target_path_abs = os.path.join(TARGET_ROOT, rel_path)
        
        current_hash = get_file_hash(source_path)
        stored_hash = state.get(rel_path)
        
        reason = None
        if force:
            reason = "Forced"
        elif stored_hash != current_hash:
            reason = "Modified" if stored_hash else "New"
        elif not os.path.exists(target_path_abs):
            reason = "Missing Target"
        
        if reason:
            files_to_translate.append({
                "source": source_path,
                "target": target_path_abs,
                "relative": rel_path,
                "current_hash": current_hash,
                "reason": reason
            })
            
    return files_to_translate

def mark_as_translated(rel_path, hash_val):
    state = load_state()
    state[rel_path] = hash_val
    save_state(state)
    print(f"Updated state for {rel_path}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('action', choices=['scan', 'update'])
    parser.add_argument('--file', help='Relative path of the file to update (for update action)', required=False)
    parser.add_argument('--hash', help='Hash value to set (for update action)', required=False)
    parser.add_argument('--path', help='Specific path (file or dir) to scan', required=False)
    parser.add_argument('--force', action='store_true', help='Force include all files in scan')
    
    args = parser.parse_args()
    
    if args.action == 'scan':
        to_translate = get_files_to_translate(args.path, args.force)
        print(json.dumps(to_translate, indent=2, ensure_ascii=False))
        
    elif args.action == 'update':
        if not args.file or not args.hash:
            print("Error: --file and --hash are required for update action")
            sys.exit(1)
        mark_as_translated(args.file, args.hash)

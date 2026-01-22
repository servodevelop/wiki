# OMY-F3M CAD 资料库 / CAD Resources

## 1. 2D/3D 尺寸图预览 / Dimensions Preview

<div class="cad-preview-container">
    <iframe 
        src="/uart-servo/cad_files/OMY-F3M.pdf#navpanes=0&view=Fit" 
        class="pc-pdf-viewer"
        style="width: 100%; height: 100%; border: none !important; outline: none; display: block;">
    </iframe>
    
    <a href="/uart-servo/cad_files/OMY-F3M.pdf" target="_blank" class="mobile-pdf-link">
        <img src="/uart-servo/cad_files/OMY-F3M_preview.jpg" alt="Click to View PDF" class="mobile-preview-img">
        <div class="mobile-hint">点击查看全幅 PDF / Click to View Full PDF</div>
    </a>
</div>

---

## 2. 资源下载 / Resource Download

### 中文版资源 (CN)
| 格式 | 更新日期 | 大小 | 操作 |
| :---: | :---: | :---: | :---: |
| **.PDF** | <span class="no-wrap">2025-09-26</span> | 1.2 MB | <a href="/uart-servo/cad_files/OMY-F3M.pdf" class="fs-download-btn">立即下载</a> |
| **.STEP** | <span class="no-wrap">2025-09-26</span> | 4.5 MB | <a href="/uart-servo/cad_files/OMY-F3M.step" class="fs-download-btn">立即下载</a> |
| **.DWG** | <span class="no-wrap">2025-09-26</span> | 2.8 MB | <a href="/uart-servo/cad_files/OMY-F3M.dwg" class="fs-download-btn">立即下载</a> |

### English Version (EN)
| Format | Update Date | Size | Action |
| :---: | :---: | :---: | :---: |
| **.PDF** | <span class="no-wrap">2025-09-26</span> | 1.2 MB | <a href="/uart-servo/cad_files/OMY-F3M.pdf" class="fs-download-btn">DOWNLOAD</a> |
| **.STEP** | <span class="no-wrap">2025-09-26</span> | 4.5 MB | <a href="/uart-servo/cad_files/OMY-F3M.step" class="fs-download-btn">DOWNLOAD</a> |
| **.DWG** | <span class="no-wrap">2025-09-26</span> | 2.8 MB | <a href="/uart-servo/cad_files/OMY-F3M.dwg" class="fs-download-btn">DOWNLOAD</a> |

<style>
/* 1. 预览容器基础样式 */
.cad-preview-container {
    width: 100%; 
    aspect-ratio: 1.5 / 1; 
    margin: 0 auto;
    overflow: hidden;
    border: 0.5px solid var(--fs-divider); /* 匹配全局细边框 */
    border-radius: 4px;
    background: #f8f9fa;
    position: relative;
}

/* 2. 元素显示逻辑控制 */
.mobile-pdf-link { display: none; } /* 默认隐藏手机版 */

/* 日期不换行类 */
.no-wrap { white-space: nowrap !important; }

/* 3. 移动端媒体查询 (小于 768px) */
@media screen and (max-width: 768px) {
    /* 切换显示：隐藏 PDF 框，显示图片预览 */
    .pc-pdf-viewer { display: none !important; }
    .mobile-pdf-link { 
        display: block; 
        width: 100%; 
        height: 100%; 
        text-decoration: none;
    }
    
    .cad-preview-container {
        aspect-ratio: 1.66 / 1; 
    }

    .mobile-preview-img {
        width: 100%;
        height: 100%;
        object-fit: contain; /* 保证预览图在框内完整显示 */
    }

    .mobile-hint {
        position: absolute;
        bottom: 0;
        width: 100%;
        background: rgba(0,0,0,0.6);
        color: #fff;
        font-size: 12px;
        text-align: center;
        padding: 4px 0;
    }

    /* 手机端表格字体微调 */
    .md-typeset table td {
        font-size: 13px !important;
        padding: 8px 4px !important;
    }
}
</style>
 <style>
/* 1. 预览容器样式 - 仅保留布局，移除装饰，由内部 img 的全局 Section 7 提供相框效果 */
.cad-preview-wrapper {
    width: 85% !important;
    margin: 20px auto;
    position: relative;
    line-height: 0; 
}

/* PDF 的比例和独立边框 */
.desktop-pdf-embed { 
    aspect-ratio: 1.28 / 1; 
    display: block; 
    border: 0.5px solid var(--fs-divider);
    border-radius: 4px;
}

.mobile-image-link { display: none; width: 100%; }
/* 重点：移动端图片样式由 Section 7 接管 */
.mobile-image-link img { 
    max-width: 100% !important; 
    margin: 0 auto !important; 
}

/* 2. 表格与不换行深度锁定 */
.table-container table { border-collapse: collapse !important; border: 0.8px solid var(--fs-divider) !important; }
.table-container th, .table-container td { border: 0.8px solid var(--fs-divider) !important; vertical-align: middle !important; }

/* 强制列表不换行逻辑 */
.no-wrap-cell {
    background: var(--fs-bg-active) !important;
    padding: 0 10px 0 5px !important; 
    white-space: nowrap !important;
}

.no-wrap-cell ul {
    margin: 0 !important; 
    padding: 0 0 0 0.8em !important; 
    list-style-type: disc; 
    font-size: 14.5px; 
    line-height: 1.8;
}

.no-wrap-cell ul li, .no-wrap-cell ul li a, .no-wrap-cell strong {
    white-space: nowrap !important; /* 确保移动端不挤压换行 */
}

.table-container { width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch; }
.hide-scrollbar::-webkit-scrollbar { display: none; }
.hide-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }

/* 4. 移动端适配 */
@media screen and (max-width: 1024px) {
    .cad-preview-wrapper { width: 100% !important; margin: 10px 0; }
    .desktop-pdf-embed { display: none !important; }
    .mobile-image-link { display: block !important; }
    .md-typeset table td { padding: 8px 5px !important; }
    .no-wrap-cell ul { padding-left: 0.7em !important; }
}
</style>

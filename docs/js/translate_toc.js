document.addEventListener("DOMContentLoaded", function() {
  function updateTocTitle() {
    // 找到右侧目录的标题元素
    const tocTitle = document.querySelector(".md-nav--secondary .md-nav__title");
    if (!tocTitle) return;

    // 获取当前页面语言（由 i18n 插件自动注入到 html 标签）
    const lang = document.documentElement.lang || "en";

    const translations = {
      "en": "On this page",
      "es": "En esta página",
      "fr": "Sur cette page",
      "de": "Auf dieser Seite",
      "ja": "このページの内容"
    };

    // 替换文字，保留原来的 HTML 结构（如有图标等）
    const newText = translations[lang] || translations["en"];
    
    // 精准替换文本节点
    for (const node of tocTitle.childNodes) {
      if (node.nodeType === Node.TEXT_NODE && node.textContent.trim() !== "") {
        node.textContent = newText;
        break;
      }
    }
  }

  // 立即执行
  updateTocTitle();
  // 兼容 Material 的即时加载模式
  if (typeof subscribe === "function") {
    subscribe(updateTocTitle);
  }
});

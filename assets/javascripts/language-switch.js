document.addEventListener("DOMContentLoaded", function() {
  const langLinks = document.querySelectorAll(".md-select__link");
  langLinks.forEach(link => {
    link.addEventListener("click", function(e) {
      e.preventDefault();
      const targetLang = this.getAttribute("hreflang");
      const currentPath = window.location.pathname;
      
      let newPath = "";
      if (targetLang === "zh") {
        // 如果当前不在 zh 目录下，切往 zh
        newPath = currentPath.startsWith("/zh/") ? currentPath : "/zh" + currentPath;
      } else {
        // 如果当前在 zh 目录下，切回根目录
        newPath = currentPath.startsWith("/zh/") ? currentPath.replace("/zh/", "/") : currentPath;
      }
      
      // 修正双斜杠问题
      newPath = newPath.replace(/\/+/g, '/');
      window.location.href = newPath;
    });
  });
});
// 自动原地切换语言脚本
document.addEventListener("DOMContentLoaded", function() {
  // 找到所有语言切换链接
  const links = document.querySelectorAll(".md-select__link");
  
  links.forEach(link => {
    link.addEventListener("click", function(event) {
      event.preventDefault(); // 拦截默认的首页跳转行为
      
      const targetLang = this.getAttribute("hreflang");
      const currentPath = window.location.pathname;
      let newPath = "";

      if (targetLang === "zh") {
        // 如果当前不在 /zh/ 路径下，则在路径前加上 /zh/
        if (!currentPath.startsWith("/zh/")) {
          newPath = "/zh" + currentPath;
        } else {
          newPath = currentPath;
        }
      } else {
        // 如果当前在 /zh/ 路径下，则移除开头的 /zh/
        if (currentPath.startsWith("/zh/")) {
          newPath = currentPath.replace("/zh/", "/");
        } else {
          newPath = currentPath;
        }
      }

      // 清理可能产生的双斜杠 //
      newPath = newPath.replace(/\/+/g, '/');
      window.location.href = newPath;
    });
  });
});
"use strict";
(() => {
  const toggle = document.querySelector(".nav-toggle");
  toggle?.addEventListener("click", () => {
    const open = document.body.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", String(open));
  });
  document.querySelectorAll(".book-sidebar a").forEach(a => a.addEventListener("click", () => {
    document.body.classList.remove("nav-open");
    toggle?.setAttribute("aria-expanded", "false");
  }));
  document.querySelector("#toc-filter")?.addEventListener("input", event => {
    const query = event.target.value.toLocaleLowerCase().trim();
    document.querySelectorAll(".book-sidebar li").forEach(li => {
      li.hidden = !li.textContent.toLocaleLowerCase().includes(query);
    });
  });
  async function copyText(value) {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(value);
      return;
    }
    // The file:// offline book also works in browsers without Clipboard API.
    const text = document.createElement("textarea");
    text.value = value;
    text.style.cssText = "position:fixed;left:-10000px;top:0";
    document.body.append(text);
    text.select();
    const copied = document.execCommand("copy");
    text.remove();
    if (!copied) throw new Error("copy unavailable");
  }
  document.querySelectorAll("pre").forEach(pre => {
    const wrapper = document.createElement("div");
    wrapper.className = "code-shell";
    pre.replaceWith(wrapper);
    wrapper.append(pre);
    const button = document.createElement("button");
    button.type = "button";
    button.className = "copy-code";
    button.textContent = "复制代码";
    button.addEventListener("click", async () => {
      try {
        await copyText(pre.textContent);
        button.textContent = "已复制";
      } catch (_) {
        button.textContent = "请选择代码复制";
      }
      setTimeout(() => { button.textContent = "复制代码"; }, 2000);
    });
    wrapper.append(button);
  });
  document.querySelectorAll("table").forEach(table => {
    const wrapper = document.createElement("div");
    wrapper.className = "table-scroll";
    table.replaceWith(wrapper);
    wrapper.append(table);
  });
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(entries => {
      const visible = entries.filter(entry => entry.isIntersecting).sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      if (!visible.length) return;
      const id = visible[0].target.querySelector("h1")?.id;
      document.querySelectorAll(".book-sidebar a[aria-current]").forEach(a => a.removeAttribute("aria-current"));
      const active = document.querySelector('.book-sidebar a[href="#' + CSS.escape(id || "") + '"]');
      active?.setAttribute("aria-current", "location");
    }, {rootMargin: "-5% 0px -70% 0px"});
    document.querySelectorAll(".book-chapter").forEach(chapter => observer.observe(chapter));
  }
})();

/*
  manages Chinese/English language toggle for header labels.
*/

{
  const storageKey = "site-lang";
  const defaultLang = "zh";

  const getLang = () => window.localStorage.getItem(storageKey) ?? defaultLang;
  const getDict = (lang) => (window.I18N || {})[lang] || {};

  const resolveKey = (key, lang) => {
    if (!key) {
      return null;
    }

    return key.split(".").reduce((value, part) => {
      if (!value || part === "") {
        return null;
      }
      return value[part];
    }, getDict(lang));
  };

  const updateMeta = (lang) => {
    const root = document.documentElement;
    const pageTitleKey = root.dataset.i18nPageTitle;
    const siteTitleKey = root.dataset.i18nSiteTitle;
    const descriptionKey = root.dataset.i18nDescription;
    const fallbackTitle = root.dataset.pageTitleFallback;
    const fallbackDescription = root.dataset.pageDescriptionFallback;

    const pageTitle = resolveKey(pageTitleKey, lang) || fallbackTitle || document.title;
    const siteTitle = resolveKey(siteTitleKey, lang) || "";
    const description = resolveKey(descriptionKey, lang) || fallbackDescription || "";

    const fullTitle =
      siteTitle && pageTitle && pageTitle !== siteTitle
        ? `${pageTitle} | ${siteTitle}`
        : pageTitle || siteTitle;

    if (fullTitle) {
      document.title = fullTitle;
    }

    const setMeta = (attr, name, content) => {
      if (!content) {
        return;
      }
      const element = document.querySelector(`meta[${attr}='${name}']`);
      if (element) {
        element.setAttribute("content", content);
      }
    };

    setMeta("name", "title", pageTitle);
    setMeta("name", "description", description);
    setMeta("property", "og:title", pageTitle);
    setMeta("property", "og:site_title", siteTitle);
    setMeta("property", "og:description", description);
    setMeta("property", "og:locale", lang === "zh" ? "zh_CN" : "en_US");
    setMeta("property", "twitter:title", pageTitle);
    setMeta("property", "twitter:description", description);
  };

  const applyLang = (lang) => {
    document.documentElement.lang = lang;
    document.documentElement.dataset.lang = lang;

    document.querySelectorAll("[data-i18n]").forEach((element) => {
      const value = resolveKey(element.dataset.i18n, lang);
      if (value) {
        element.textContent = value;
      }
    });

    document.querySelectorAll("[data-i18n-placeholder]").forEach((element) => {
      const value = resolveKey(element.dataset.i18nPlaceholder, lang);
      if (value) {
        element.setAttribute("placeholder", value);
      }
    });

    document.querySelectorAll("[data-i18n-aria]").forEach((element) => {
      const value = resolveKey(element.dataset.i18nAria, lang);
      if (value) {
        element.setAttribute("aria-label", value);
      }
    });

    document.querySelectorAll("[data-i18n-tooltip]").forEach((element) => {
      const value = resolveKey(element.dataset.i18nTooltip, lang);
      if (value) {
        element.setAttribute("data-tooltip", value);
      }
    });

    document
      .querySelectorAll("[data-i18n-tooltip-template][data-tag]")
      .forEach((element) => {
        const template = resolveKey(element.dataset.i18nTooltipTemplate, lang);
        if (template) {
          element.setAttribute(
            "data-tooltip",
            template.replace("{tag}", element.dataset.tag || "")
          );
        }
      });

    const toggle = document.querySelector(".lang-toggle");
    if (toggle) {
      const isZh = lang === "zh";
      toggle.textContent = isZh ? "EN" : "中文";
      toggle.setAttribute("aria-label", isZh ? "Switch to English" : "切换为中文");
    }

    updateMeta(lang);
    window.dispatchEvent(new Event("languagechange"));
  };

  const setLang = (lang) => {
    window.localStorage.setItem(storageKey, lang);
    applyLang(lang);
  };

  const setupToggle = () => {
    const toggle = document.querySelector(".lang-toggle");
    if (!toggle) {
      return;
    }

    toggle.addEventListener("click", () => {
      const next = getLang() === "zh" ? "en" : "zh";
      setLang(next);
    });
  };

  applyLang(getLang());
  window.addEventListener("load", () => {
    applyLang(getLang());
    setupToggle();
  });
}
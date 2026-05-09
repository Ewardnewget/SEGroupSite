---
title: Contact
i18n_title: contact.title
i18n_description: contact.description
nav:
  order: 5
  tooltip: Email, address, and location
---

<p data-i18n="contact.intro">{% include i18n-text.html key="contact.intro" %}</p>

{%
  include button.html
  type="email"
  text="yancai@ios.ac.cn"
  link="mailto:yancai@ios.ac.cn"
%}

<p>{% include icon.html icon="fa-solid fa-map-location-dot" %} 北京市海淀区中关村南四街4号 中国科学院软件研究所</p>


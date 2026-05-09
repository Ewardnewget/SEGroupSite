---
title: Contact
i18n_title: contact.title
i18n_description: contact.description
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}<span data-i18n="contact.title">{% include i18n-text.html key="contact.title" %}</span>
<p data-i18n="contact.intro">{% include i18n-text.html key="contact.intro" %}</p>

{%
  include button.html
  type="email"
  text="yancai@ios.ac.cn"
  link="mailto:yancai@ios.ac.cn"
%}
{% capture location_tooltip %}{% include i18n-text.html key='contact.location_tooltip' %}{% endcapture %}
{%
  include button.html
  type="address"
  i18nTooltip="contact.location_tooltip"
  tooltip=location_tooltip
  link="https://www.google.com/maps"
%}


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
  text="jane@smith.com"
  link="jane@smith.com"
%}
{%
  include button.html
  type="phone"
  text="(555) 867-5309"
  link="+1-555-867-5309"
%}
{% capture location_tooltip %}{% include i18n-text.html key='contact.location_tooltip' %}{% endcapture %}
{%
  include button.html
  type="address"
  i18nTooltip="contact.location_tooltip"
  tooltip=location_tooltip
  link="https://www.google.com/maps"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/photo.jpg"
  i18nCaption="contact.figure_caption"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/photo.jpg"
  i18nCaption="contact.figure_caption"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}

{% include section.html dark=true %}

{% capture col1 %}
<span data-i18n="contact.col1">{% include i18n-text.html key="contact.col1" %}</span>
{% endcapture %}

{% capture col2 %}
<span data-i18n="contact.col2">{% include i18n-text.html key="contact.col2" %}</span>
{% endcapture %}

{% capture col3 %}
<span data-i18n="contact.col3">{% include i18n-text.html key="contact.col3" %}</span>
{% endcapture %}

{% include cols.html col1=col1 col2=col2 col3=col3 %}

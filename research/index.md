---
title: Research
i18n_title: research.title
i18n_description: research.description
nav:
  order: 1
  tooltip: Published works
---

# {% include icon.html icon="fa-solid fa-microscope" %}<span data-i18n="research.title">{% include i18n-text.html key="research.title" %}</span>

<p data-i18n="research.intro">{% include i18n-text.html key="research.intro" %}</p>

{% include section.html %}

## <span data-i18n="research.highlighted">{% include i18n-text.html key="research.highlighted" %}</span>

{% include citation.html lookup="Open collaborative writing with Manubot" style="rich" %}

{% include section.html %}

## <span data-i18n="research.all">{% include i18n-text.html key="research.all" %}</span>

{% include search-box.html %}

{% include search-info.html %}

{% include list.html data="citations" component="citation" style="rich" %}

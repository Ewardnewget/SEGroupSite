---
title: Projects
i18n_title: projects.title
i18n_description: projects.description
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}<span data-i18n="projects.title">{% include i18n-text.html key="projects.title" %}</span>

<p data-i18n="projects.intro">{% include i18n-text.html key="projects.intro" %}</p>
{% include tags.html tags="publication, resource, website" %}

{% include search-info.html %}

{% include section.html %}

## <span data-i18n="projects.featured">{% include i18n-text.html key="projects.featured" %}</span>

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include section.html %}

## <span data-i18n="projects.more">{% include i18n-text.html key="projects.more" %}</span>

{% include list.html component="card" data="projects" filter="!group" style="small" %}

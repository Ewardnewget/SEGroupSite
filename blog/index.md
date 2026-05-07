---
title: Blog
i18n_title: blog.title
i18n_description: blog.description
nav:
  order: 4
  tooltip: Musings and miscellany
---

# {% include icon.html icon="fa-solid fa-feather-pointed" %}<span data-i18n="blog.title">{% include i18n-text.html key="blog.title" %}</span>

<p data-i18n="blog.intro">{% include i18n-text.html key="blog.intro" %}</p>

{% include section.html %}

{% include search-box.html %}

{% include tags.html tags=site.tags %}

{% include search-info.html %}

{% include list.html data="posts" component="post-excerpt" %}

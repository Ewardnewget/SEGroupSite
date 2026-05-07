---
title: Team
i18n_title: team.title
i18n_description: team.description
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}<span data-i18n="team.title">{% include i18n-text.html key="team.title" %}</span>

<p data-i18n="team.intro">{% include i18n-text.html key="team.intro" %}</p>

{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}
{% include list.html data="members" component="portrait" filter="role != 'pi'" %}

{% include section.html background="images/background.jpg" dark=true %}

<p data-i18n="team.section_intro">{% include i18n-text.html key="team.section_intro" %}</p>

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" i18nCaption="team.gallery_caption" %}
{% include figure.html image="images/photo.jpg" i18nCaption="team.gallery_caption" %}
{% include figure.html image="images/photo.jpg" i18nCaption="team.gallery_caption" %}

{% endcapture %}

{% include grid.html style="square" content=content %}

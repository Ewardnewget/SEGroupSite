---
i18n_title: home.title
i18n_description: home.intro
---

# <span data-i18n="home.title">{% include i18n-text.html key="home.title" %}</span>

<p data-i18n="home.intro">{% include i18n-text.html key="home.intro" %}</p>

{% include section.html %}

## <span data-i18n="home.highlights">{% include i18n-text.html key="home.highlights" %}</span>

{% capture text %}

<p data-i18n="home.research_text">{% include i18n-text.html key="home.research_text" %}</p>

{%
  include button.html
  link="research"
  text=site.data.i18n.zh.home.research_button
  i18n="home.research_button"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="research"
  title=site.data.i18n.zh.home.research_title
  i18nTitle="home.research_title"
  text=text
%}

{% capture text %}

<p data-i18n="home.projects_text">{% include i18n-text.html key="home.projects_text" %}</p>

{%
  include button.html
  link="projects"
  text=site.data.i18n.zh.home.projects_button
  i18n="home.projects_button"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="projects"
  title=site.data.i18n.zh.home.projects_title
  i18nTitle="home.projects_title"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

<p data-i18n="home.team_text">{% include i18n-text.html key="home.team_text" %}</p>

{%
  include button.html
  link="team"
  text=site.data.i18n.zh.home.team_button
  i18n="home.team_button"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/photo.jpg"
  link="team"
  title=site.data.i18n.zh.home.team_title
  i18nTitle="home.team_title"
  text=text
%}

---
title: Home
i18n_title: home.title
i18n_description: home.intro
---

<h1 class="center" data-i18n="home.title">{% include i18n-text.html key="home.title" %}</h1>
<p class="center" data-i18n="home.intro">{% include i18n-text.html key="home.intro" %}</p>

{% include section.html dark=true %}
<h2 class="center" data-i18n="home.research_title">{% include i18n-text.html key="home.research_title" %}</h2>
{% capture col1 %}{% include card.html image="images/analysis.jpg" title="Program Analysis" description="Describe research area one." %}{% endcapture %}
{% capture col2 %}{% include card.html image="images/testing.jpg" title="Software Testing" description="Describe research area two." %}{% endcapture %}
{% capture col3 %}{% include card.html image="images/ai.png" title="AI & SE" description="Describe research area three." %}{% endcapture %}
{% include cols.html col1=col1 col2=col2 col3=col3 %}
{% include section.html %}

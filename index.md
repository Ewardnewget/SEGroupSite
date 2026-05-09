---
i18n_title: home.title
i18n_description: home.intro
---

<h1 class="center" data-i18n="home.title">{% include i18n-text.html key="home.title" %}</h1>

<p class="center" data-i18n="home.intro">{% include i18n-text.html key="home.intro" %}</p>

{% include section.html dark=true %}

<h2 class="center" data-i18n="home.research_title">{% include i18n-text.html key="home.research_title" %}</h2>

{% capture col1 %}
{% include card.html image="images/analysis.jpg" title="程序分析" description="研究 C/C++ 、Java等编程语言的程序静态分析、自动推理和约束求解技术，提供高精度的静态分析解决方案。" %}
{% endcapture %}
{% capture col2 %}
{% include card.html image="images/testing.jpg" title="软件测试" description="面向并发软件、移动应用、操作系统等应用场景，研究动态测试技术，提供全自动的一体化流程测试解决方案。" %}
{% endcapture %}
{% capture col3 %}
{% include card.html image="images/ai.png" title="人工智能系统分析与测试" description="研究多智能体系统、自动驾驶系统、代码大模型、LLM Agent等应用的分析与测试，结合AI与传统软件工程，探索AI4SE与SE4AI两个方向。" %}
{% endcapture %}
<div class="home-cards home-cards--research">
{% include cols.html col1=col1 col2=col2 col3=col3 %}
</div>

{% include section.html %}

<h2 class="center" data-i18n="home.team_title">{% include i18n-text.html key="home.team_title" %}</h2>

{% capture col1 %}
{% include card.html title="职工" description="国家杰青在内的高水平团队，职工9人。" link="team/#faculty" %}
{% endcapture %}
{% capture col2 %}
{% include card.html title="学生" description="在培学生数十人，拥有完善的硕博培养体系。" link="team/#students" %}
{% endcapture %}
{% capture col3 %}
{% include card.html title="毕业生" description="已培养学生过百人，入职华为、字节、腾讯、科研院所、国央企等企事业单位，多位获得国家奖学金、北京市优秀毕业生等荣誉称号。" link="team/#alumni" %}
{% endcapture %}
<div class="home-cards home-cards--team">
{% include cols.html col1=col1 col2=col2 col3=col3 %}
</div>

{% include section.html dark=true %}

<h2 class="center" data-i18n="home.projects_title">{% include i18n-text.html key="home.projects_title" %}</h2>

{% capture col1 %}
{% include card.html image="images/photo.jpg" title="刊物发表" description="在软件工程、形式化、人工智能等领域的国际顶级会议和期刊发表论文数百篇。" link="publications" %}
{% endcapture %}
{% capture col2 %}
{% include card.html image="images/photo.jpg" title="承接项目" description="承接国家重点研发计划、国自然重点、中国科学院A类先导等国家级或省部级重点项目。" link="contact" %}
{% endcapture %}
{% capture col3 %}
{% include card.html image="images/photo.jpg" title="合作" description="与国内外知名高校（清北南大、UCLA、NUS等）以及华为、字节、阿里巴巴等业内领军企业开展广泛合作。" link="contact" %}
{% endcapture %}
<div class="home-cards home-cards--projects">
{% include cols.html col1=col1 col2=col2 col3=col3 %}
</div>

{% include section.html %}

<h2 class="center" data-i18n="home.news_title">{% include i18n-text.html key="home.news_title" %}</h2>

<br>
<ul>
  <li><strong>2026.05:</strong> 最新研究成果被软件工程领域国际顶级会议 ICSE 2026 接收。</li>
  <li><strong>2026.04:</strong> 团队成员研究成果荣获最佳论文奖。</li>
  <li><strong>2026.03:</strong> 我们研发的下一代自动推理与程序分析工具 2.0 版本已正式开源并交付给行业合作伙伴使用。</li>
</ul>


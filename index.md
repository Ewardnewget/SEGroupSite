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

{% capture team_text %}
团队汇聚了包括国家杰青在内的9名高水平科研人员。目前在培硕博学生30余人，拥有完善的培养体系；已培养毕业生60余人，多数入职华为、字节、腾讯、大院大所、国央企等企事业单位，多名同学曾获得国家奖学金、北京市优秀毕业生等荣誉称号。

{% include button.html text="了解团队" link="team" %}
{% endcapture %}

{% include feature.html image="images/students.jpg" i18nTitle="home.team_title" text=team_text %}

{% include section.html dark=true %}

{% capture projects_text %}
团队在软件工程、形式化方法、人工智能等领域的国际顶级会议和期刊上发表高水平论文数百篇。先后承接了国家重点研发计划、国家自然科学基金重点项目、中国科学院A类先导等国家级或省部级重大科研任务。同时，与国内外知名高校（如清北南大、UCLA、NUS等）以及华为、字节、阿里巴巴等业内领军企业持续开展深度广泛的合作。

{% include button.html text="更多成果" link="publications" %}
{% endcapture %}

{% include feature.html image="images/Papers.jpg" i18nTitle="home.projects_title" text=projects_text %}

{% include section.html %}

<h2 class="center" data-i18n="home.news_title">{% include i18n-text.html key="home.news_title" %}</h2>

<br>
<ul>
  <li><strong>2026.05:</strong> 1篇论文被人工智能领域国际顶级会议 ICML 2026 录用。</li>
  <li><strong>2026.04:</strong> 最新研究成果被软件工程领域国际顶级会议 ISSTA 2026 录用。</li>
  <li><strong>2025.07:</strong> 张健研究院荣获 QRS 二十五周年特别荣誉奖。</li>
</ul>

<div style="text-align: center; margin-top: 30px;">
{% include button.html text="更多动态" link="news" %}
</div>


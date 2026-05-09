---
title: Tools
i18n_title: projects.title
i18n_description: projects.description
published: false
nav:
  order: 4
  tooltip: Tools and resources
---

<h1 class="center" data-i18n="projects.title">{% include i18n-text.html key="projects.title" %}</h1>

<p class="center" data-i18n="projects.intro">{% include i18n-text.html key="projects.intro" %}</p>

{% include section.html dark=true %}

<style>
/* CSS for Tabs */
.tab-container {
  max-width: 1200px;
  margin: 0 auto;
}

.tab-nav {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.tab-btn {
  background: var(--background);
  color: var(--text);
  border: 1px solid var(--text);
  padding: 8px 16px;
  border-radius: 20px;
  cursor: pointer;
  transition: background 0.2s, color 0.2s;
  font-weight: bold;
}

.tab-btn.active, .tab-btn:hover {
  background: var(--text);
  color: var(--background);
}

.tab-content {
  display: none;
}

.tab-content.active {
  display: block;
  animation: fadeEffect 0.5s;
}

@keyframes fadeEffect {
  from {opacity: 0;}
  to {opacity: 1;}
}

/* Card overrides for tools */
.tool-card {
  display: flex;
  align-items: center;
  background: var(--background);
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  gap: 1.5rem;
}

.tool-img {
  width: 150px;
  max-height: 100px;
  object-fit: cover;
  border-radius: 4px;
}

.tool-info h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
}

.tool-info p {
  margin: 0;
  margin-bottom: 0.5rem;
  color: var(--text-light);
}

@media (max-width: 600px) {
  .tool-card {
    flex-direction: column;
    text-align: center;
  }
}
</style>

<div class="tab-container">
  <div class="tab-nav">
    <button class="tab-btn active" onclick="openTab(event, 'tab-analysis')">程序分析</button>
    <button class="tab-btn" onclick="openTab(event, 'tab-testing')">软件测试</button>
    <button class="tab-btn" onclick="openTab(event, 'tab-ai')">AI 与 SE</button>
  </div>

  <div id="tab-analysis" class="tab-content active">
    
    <div class="tool-card">
      <img class="tool-img" src="{{ 'images/photo.jpg' | relative_url }}" alt="Tool A">
      <div class="tool-info">
        <h3>AnalysisTool A</h3>
        <p>高精度的 C/C++ 静态分析框架，支持跨文件的数据流与控制流追踪。</p>
        <a href="#" class="button bare"><i class="fa-solid fa-link"></i> 访问项目</a>
        <a href="#" class="button bare"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>

    <div class="tool-card">
      <img class="tool-img" src="{{ 'images/photo.jpg' | relative_url }}" alt="Tool B">
      <div class="tool-info">
        <h3>Solver B</h3>
        <p>支持多理论融合的高效约束求解器，在工业级代码验证中发挥关键作用。</p>
        <a href="#" class="button bare"><i class="fa-solid fa-link"></i> 访问项目</a>
      </div>
    </div>

  </div>

  <div id="tab-testing" class="tab-content">
    
    <div class="tool-card">
      <img class="tool-img" src="{{ 'images/photo.jpg' | relative_url }}" alt="Tool C">
      <div class="tool-info">
        <h3>FuzzingFramework C</h3>
        <p>现代化的动态模糊测试框架，支持多种变异策略和分布式部署。</p>
        <a href="#" class="button bare"><i class="fa-brands fa-github"></i> GitHub</a>
      </div>
    </div>

  </div>

  <div id="tab-ai" class="tab-content">
    
    <div class="tool-card">
      <img class="tool-img" src="{{ 'images/photo.jpg' | relative_url }}" alt="Tool D">
      <div class="tool-info">
        <h3>LLMAgent D</h3>
        <p>基于大语言模型的自动化软件开发与测试 Agent 平台。</p>
        <a href="#" class="button bare"><i class="fa-solid fa-link"></i> 立即体验</a>
      </div>
    </div>

  </div>
</div>

<script>
function openTab(evt, tabName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tab-content");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
    tabcontent[i].className = tabcontent[i].className.replace(" active", "");
  }
  tablinks = document.getElementsByClassName("tab-btn");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  document.getElementById(tabName).className += " active";
  evt.currentTarget.className += " active";
}
</script>

{% include section.html %}


---
title: Team
i18n_title: team.title
i18n_description: team.description
---

<style>
.members-grid { display: grid; gap: 20px; margin: 40px 0; width: 100%; }
.members-grid-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
.members-grid-5 { grid-template-columns: repeat(5, minmax(0, 1fr)); }
@media (max-width: 700px) { .members-grid-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .members-grid-5 { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 500px) { .members-grid-4, .members-grid-5 { grid-template-columns: 1fr; } }
.member-card { display: flex; flex-direction: column; align-items: center; text-align: center; }
.member-photo { width: 120px; aspect-ratio: 3 / 4; object-fit: cover; border-radius: 8px; margin-bottom: 15px; }
.member-name { font-family: var(--heading); font-weight: var(--semi-bold); font-size: 1.1em; margin-bottom: 5px; }
.member-desc { font-size: 0.9em; color: var(--text-light, #555); margin-bottom: 15px; flex-grow: 1; }
.member-links { display: flex; gap: 15px; justify-content: center; }
.member-links a { color: var(--text); font-size: 1.2em; transition: opacity 0.2s; }
.member-links a:hover { opacity: 0.7; }
.table-container { width: 100%; overflow-x: auto; margin: 40px 0; }
.alumni-table { width: 100%; border-collapse: collapse; }
.alumni-table th { background-color: var(--light-gray, #eaeaea); padding: 12px; text-align: center; }
.alumni-table td { padding: 12px; border-bottom: 1px solid var(--light-gray, #eaeaea); text-align: center; }
.sub-section-title { margin-top: 30px; margin-bottom: 15px; font-size: 1.3em; font-weight: bold; border-left: 4px solid var(--text); padding-left: 10px; }
</style>

<h1 data-i18n="team.title">{% include i18n-text.html key="team.title" %}</h1>
<p data-i18n="team.intro">{% include i18n-text.html key="team.intro" %}</p>

{% include section.html dark=true %}

<h2 id="faculty">教职工</h2>
<div class="sub-section-title">负责人</div>
<div class="members-grid members-grid-4">
  <div class="member-card">
    <img src="{{ 'images/蔡彦.jpg' | relative_url }}" class="member-photo" alt="蔡彦">
    <div class="member-name">蔡彦</div>
    <div class="member-desc">研究员，博导，研究室主任</div>
    <div class="member-links">
      <a href="https://yancai.site/" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:yancai@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

<div class="sub-section-title">资深专家</div>
<div class="members-grid members-grid-4">
  <div class="member-card">
    <img src="{{ 'images/张健.jpg' | relative_url }}" class="member-photo" alt="张健">
    <div class="member-name">张健</div>
    <div class="member-desc">研究员，博导，国家杰青</div>
    <div class="member-links">
      <a href="https://lcs.ios.ac.cn/~zj/zj_chn.html" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:zj@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

<div class="sub-section-title">成员</div>
<div class="members-grid members-grid-4">
  <div class="member-card">
    <img src="{{ 'images/晏荣杰.jpg' | relative_url }}" class="member-photo" alt="晏荣杰">
    <div class="member-name">晏荣杰</div>
    <div class="member-desc">副研究员，硕导</div>
    <div class="member-links">
      <a href="https://people.ucas.edu.cn/~yanrj" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:yrj@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
    <div class="member-card">
    <img src="{{ 'images/吴鹏.jpg' | relative_url }}" class="member-photo" alt="吴鹏">
    <div class="member-name">吴鹏</div>
    <div class="member-desc">副研究员，硕导</div>
    <div class="member-links">
      <a href="https://people.ucas.ac.cn/~wp" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:wp@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/高航.jpg' | relative_url }}" class="member-photo" alt="高航">
    <div class="member-name">高航</div>
    <div class="member-desc">高级工程师</div>
    <div class="member-links">
      <a href="https://orcid.org/0000-0003-3613-4011" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:gaohang@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
    <div class="member-card">
    <img src="{{ 'images/王静华.jpg' | relative_url }}" class="member-photo" alt="王静华">
    <div class="member-name">王静华</div>
    <div class="member-desc">工程师</div>
    <div class="member-links">
      <a href="mailto:wangjh@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/瞿荣.jpg' | relative_url }}" class="member-photo" alt="瞿荣">
    <div class="member-name">瞿荣</div>
    <div class="member-desc">工程师</div>
    <div class="member-links">
      <a href="mailto:qurong@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

<div class="sub-section-title">博士后</div>
<div class="members-grid members-grid-4">
  <div class="member-card">
    <img src="{{ 'images/崔保全.jpg' | relative_url }}" class="member-photo" alt="崔保全">
    <div class="member-name">崔保全</div>
    <div class="member-desc">博士后</div>
    <div class="member-links">
      <a href="https://cuixiaoyiyi.github.io/" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:cuibq@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/祝世豪.jpg' | relative_url }}" class="member-photo" alt="祝世豪">
    <div class="member-name">祝世豪</div>
    <div class="member-desc">博士后</div>
    <div class="member-links">
      <a href="mailto:zhush@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

{% include section.html %}

<h2 id="students">在培学生</h2>
<div class="sub-section-title">博士生</div>
<div class="members-grid members-grid-5">
  <div class="member-card">
    <img src="{{ 'images/张豪.jpg' | relative_url }}" class="member-photo" alt="张豪">
    <div class="member-name">张豪</div>
    <div class="member-desc">2019 - 现在</div>
    <div class="member-links">
      <a href="mailto:zhanghao19@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/张震.jpg' | relative_url }}" class="member-photo" alt="张震">
    <div class="member-name">张震</div>
    <div class="member-desc">2019 - 现在</div>
    <div class="member-links">
      <a href="mailto:zhangzhen19@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/孙朔.jpg' | relative_url }}" class="member-photo" alt="孙朔">
    <div class="member-name">孙朔</div>
    <div class="member-desc">2020 - 现在</div>
    <div class="member-links">
      <a href="mailto:sunshuo20@otcaix.iscas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/张旭东.jpg' | relative_url }}" class="member-photo" alt="张旭东">
    <div class="member-name">张旭东</div>
    <div class="member-desc">2020 - 现在</div>
    <div class="member-links">
      <a href="mailto:zhangxd20@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/贾富琦.jpg' | relative_url }}" class="member-photo" alt="贾富琦">
    <div class="member-name">贾富琦</div>
    <div class="member-desc">2020 - 现在</div>
    <div class="member-links">
      <a href="https://fuqi-jia.github.io" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:jiafq@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/卫思为.jpg' | relative_url }}" class="member-photo" alt="卫思为">
    <div class="member-name">卫思为</div>
    <div class="member-desc">2021 - 现在</div>
    <div class="member-links">
      <a href="mailto:weisw@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/张弛.jpg' | relative_url }}" class="member-photo" alt="张弛">
    <div class="member-name">张弛</div>
    <div class="member-desc">2021 - 现在</div>
    <div class="member-links">
      <a href="https://peb.pages.dev" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:yyzhangchi@126.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/赵润之.jpg' | relative_url }}" class="member-photo" alt="赵润之">
    <div class="member-name">赵润之</div>
    <div class="member-desc">2021 - 现在</div>
    <div class="member-links">
      <a href="mailto:zhaorz@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/郭宇祺.jpg' | relative_url }}" class="member-photo" alt="郭宇祺">
    <div class="member-name">郭宇祺</div>
    <div class="member-desc">2021 - 现在</div>
    <div class="member-links">
      <a href="mailto:guoyq@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/韩瑞.png' | relative_url }}" class="member-photo" alt="韩瑞">
    <div class="member-name">韩瑞</div>
    <div class="member-desc">2021 - 现在</div>
    <div class="member-links">
      <a href="mailto:hanrui@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/刘珺.jpg' | relative_url }}" class="member-photo" alt="刘珺">
    <div class="member-name">刘珺</div>
    <div class="member-desc">2022 - 现在</div>
    <div class="member-links">
      <a href="mailto:liuj2022@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/李知霖.jpg' | relative_url }}" class="member-photo" alt="李知霖">
    <div class="member-name">李知霖</div>
    <div class="member-desc">2022 - 现在</div>
    <div class="member-links">
      <a href="mailto:lizl@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/柴文健.jpg' | relative_url }}" class="member-photo" alt="柴文健">
    <div class="member-name">柴文健</div>
    <div class="member-desc">2022 - 现在</div>
    <div class="member-links">
      <a href="mailto:chaiwj@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/董宇航.jpg' | relative_url }}" class="member-photo" alt="董宇航">
    <div class="member-name">董宇航</div>
    <div class="member-desc">2022 - 现在</div>
    <div class="member-links">
      <a href="mailto:dongyuhang22@mails.ucas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/吕昆航.jpg' | relative_url }}" class="member-photo" alt="吕昆航">
    <div class="member-name">吕昆航</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:lvkh@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/孙天天.jpg' | relative_url }}" class="member-photo" alt="孙天天">
    <div class="member-name">孙天天</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:suntt@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/师朗辰.jpg' | relative_url }}" class="member-photo" alt="师朗辰">
    <div class="member-name">师朗辰</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:shilc@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/杨恒钦.jpg' | relative_url }}" class="member-photo" alt="杨恒钦">
    <div class="member-name">杨恒钦</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="https://forgottenfield.github.io/" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:yanghq@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/林璐霞.jpg' | relative_url }}" class="member-photo" alt="林璐霞">
    <div class="member-name">林璐霞</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:linlx@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/聂泽华.jpg' | relative_url }}" class="member-photo" alt="聂泽华">
    <div class="member-name">聂泽华</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:niezh@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/龚可.jpg' | relative_url }}" class="member-photo" alt="龚可">
    <div class="member-name">龚可</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/何甲文泽.jpg' | relative_url }}" class="member-photo" alt="何甲文泽">
    <div class="member-name">何甲文泽</div>
    <div class="member-desc">2025 - 现在</div>
    <div class="member-links">
      <a href="mailto:hjwz@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

<div class="sub-section-title">硕士生</div>
<div class="members-grid members-grid-5">
  <div class="member-card">
    <img src="{{ 'images/王锐.jpg' | relative_url }}" class="member-photo" alt="王锐">
    <div class="member-name">王锐</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:rogerthat232@outlook.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/肖瑜.jpg' | relative_url }}" class="member-photo" alt="肖瑜">
    <div class="member-name">肖瑜</div>
    <div class="member-desc">2023 - 现在</div>
    <div class="member-links">
      <a href="mailto:xiaoyu23@otcaix.iscas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/夏昌炜.jpg' | relative_url }}" class="member-photo" alt="夏昌炜">
    <div class="member-name">夏昌炜</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:xiachangwei24@mails.ucas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/时微淳.jpg' | relative_url }}" class="member-photo" alt="时微淳">
    <div class="member-name">时微淳</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="https://william4s.github.io/" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:shiweichun24@mails.ucas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/汪子横.jpg' | relative_url }}" class="member-photo" alt="汪子横">
    <div class="member-name">汪子横</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:wangziheng24@mails.ucas.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/苏琎韬.jpg' | relative_url }}" class="member-photo" alt="苏琎韬">
    <div class="member-name">苏琎韬</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:sujt@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/计理强.jpg' | relative_url }}" class="member-photo" alt="计理强">
    <div class="member-name">计理强</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="https://carlson-jlq.github.io/liqiang-ji.github.io/" aria-label="Homepage" target="_blank"><i class="fa-solid fa-house"></i></a>
      <a href="mailto:ji_liqiang_2020@163.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/郑锐.jpg' | relative_url }}" class="member-photo" alt="郑锐">
    <div class="member-name">郑锐</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:zhengrui@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/黄宣祺.jpg' | relative_url }}" class="member-photo" alt="黄宣祺">
    <div class="member-name">黄宣祺</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:huangxq@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/黄彬茹.jpg' | relative_url }}" class="member-photo" alt="黄彬茹">
    <div class="member-name">黄彬茹</div>
    <div class="member-desc">2024 - 现在</div>
    <div class="member-links">
      <a href="mailto:441748128@qq.com" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/傅艺玄.jpg' | relative_url }}" class="member-photo" alt="傅艺玄">
    <div class="member-name">傅艺玄</div>
    <div class="member-desc">2025 - 现在</div>
    <div class="member-links">
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/刘德志.jpg' | relative_url }}" class="member-photo" alt="刘德志">
    <div class="member-name">刘德志</div>
    <div class="member-desc">2025 - 现在</div>
    <div class="member-links">
      <a href="mailto:liudz@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
  <div class="member-card">
    <img src="{{ 'images/程洁玉.jpg' | relative_url }}" class="member-photo" alt="程洁玉">
    <div class="member-name">程洁玉</div>
    <div class="member-desc">2025 - 现在</div>
    <div class="member-links">
      <a href="mailto:chengjy@ios.ac.cn" aria-label="Email"><i class="fa-solid fa-envelope"></i></a>
    </div>
  </div>
</div>

{% include section.html dark=true %}

<h2 id="alumni">毕业生（2015年至今）</h2>
<div class="table-container">
  <table class="alumni-table">
    <thead>
      <tr><th>姓名</th><th>毕业年份</th><th>学位</th><th>毕业去向</th></tr>
    </thead>
    <tbody>
      <tr><td>崔保全</td><td>2025</td><td>博士</td><td>中科院软件所</td></tr>
      <tr><td>祝世豪</td><td>2025</td><td>博士</td><td>中科院软件所</td></tr>
      <tr><td>解远远</td><td>2025</td><td>硕士</td><td>百度</td></tr>
      <tr><td>马旭桐</td><td>2024</td><td>博士</td><td>法国 Inria</td></tr>
      <tr><td>胡梦泽</td><td>2024</td><td>硕士</td><td>字节跳动</td></tr>
      <tr><td>邓茜</td><td>2023</td><td>博士</td><td>华为</td></tr>
      <tr><td>刘明昊</td><td>2023</td><td>博士</td><td>牛津大学</td></tr>
      <tr><td>燕季薇</td><td>2023</td><td>博士</td><td>中科院软件所</td></tr>
      <tr><td>罗季</td><td>2023</td><td>硕士</td><td>航天研究所</td></tr>
      <tr><td>王金秋</td><td>2023</td><td>硕士</td><td>中信证券</td></tr>
      <tr><td>王苗苗</td><td>2023</td><td>硕士</td><td>蚂蚁金服</td></tr>
      <tr><td>黄沛</td><td>2022</td><td>博士</td><td>斯坦福大学</td></tr>
      <tr><td>苏静</td><td>2022</td><td>硕士</td><td>-</td></tr>
      <tr><td>王伟</td><td>2022</td><td>硕士</td><td>国家电网</td></tr>
      <tr><td>章新</td><td>2022</td><td>硕士</td><td>腾讯</td></tr>
      <tr><td>潘临杰</td><td>2021</td><td>博士</td><td>华为</td></tr>
      <tr><td>刘力铭</td><td>2021</td><td>硕士</td><td>-</td></tr>
      <tr><td>刘晴</td><td>2021</td><td>硕士</td><td>阿里巴巴</td></tr>
      <tr><td>云昊</td><td>2021</td><td>硕士</td><td>中信证券</td></tr>
      <tr><td>张龙</td><td>2020</td><td>博士</td><td>华为</td></tr>
      <tr><td>李润东</td><td>2020</td><td>硕士</td><td>微软</td></tr>
      <tr><td>李雅琪</td><td>2020</td><td>硕士</td><td>字节跳动</td></tr>
      <tr><td>孟瑞杰</td><td>2020</td><td>硕士</td><td>新加坡国立大学</td></tr>
      <tr><td>张帆</td><td>2020</td><td>硕士</td><td>百度</td></tr>
      <tr><td>葛存菁</td><td>2019</td><td>博士</td><td>奥地利林茨大学</td></tr>
      <tr><td>李海成</td><td>2019</td><td>硕士</td><td>百度</td></tr>
      <tr><td>王平</td><td>2019</td><td>硕士</td><td>腾讯</td></tr>
      <tr><td>朱碧云</td><td>2019</td><td>硕士</td><td>百度</td></tr>
      <tr><td>吴兴明</td><td>2018</td><td>博士</td><td>-</td></tr>
      <tr><td>曹玲薇</td><td>2018</td><td>硕士</td><td>阿里巴巴</td></tr>
      <tr><td>吕亦奇</td><td>2018</td><td>硕士</td><td>每日优鲜</td></tr>
      <tr><td>杨玲</td><td>2018</td><td>硕士</td><td>微软</td></tr>
      <tr><td>吴添勇</td><td>2017</td><td>博士</td><td>华为</td></tr>
      <tr><td>刘洁瑞</td><td>2017</td><td>硕士</td><td>字节跳动</td></tr>
      <tr><td>燕东</td><td>2017</td><td>硕士</td><td>百度</td></tr>
      <tr><td>卢琼</td><td>2016</td><td>硕士</td><td>微软</td></tr>
      <tr><td>张智强</td><td>2015</td><td>博士</td><td>谷歌</td></tr>
    </tbody>
  </table>
</div>

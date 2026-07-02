# Lab Website Template Export

基于 [Greene Lab Website Template](https://github.com/greenelab/lab-website-template) 的实验室网站模板导出包，包含三种使用方式。

## 目录结构

```
lab-website-template-export/
├── README.md                 # 本说明
├── wordpress/                # WordPress 主题（可直接上传安装）
│   └── lab-website-template/
├── jekyll/                   # Jekyll 源模板（GitHub Pages 等）
└── static/                   # 静态 HTML 演示（任意 Web 服务器）
```

---

## 1. WordPress 安装

1. 将 `wordpress/lab-website-template` 文件夹压缩为 **zip**（确保 zip 根目录下是 `style.css`，而非外层再套一层文件夹）。
2. 登录 WordPress 后台 → **外观** → **主题** → **添加主题** → **上传主题** → 选择 zip 并安装。
3. 启用主题后：
   - **外观 → 自定义 → Lab Theme Options**：设置联系邮箱、页眉/页脚背景图。
   - **外观 → 菜单**：创建主菜单并分配到 **Primary Menu**（不设置则使用默认链接）。
   - 将站点首页设为静态页面，或保留默认以显示 `front-page.php` 演示布局。
4. 创建页面 slug 为 `team`、`news`、`publications`、`contact` 以匹配导航链接。
5. 中英文切换：主题内置 `assets/i18n.json`，编辑该文件可修改文案；前端通过右上角语言切换（需 `lang-toggle.js`）。

### 推荐页面结构

| 页面 | 建议 slug | 说明 |
|------|-----------|------|
| 首页 | （设为静态首页） | 使用主题自带 front-page 布局 |
| 团队 | team | 成员网格、毕业生表格 |
| 新闻 | news | 新闻列表 |
| 出版物 | publications | 论文/书籍列表 |
| 联系 | contact | 地址与邮箱 |

---

## 2. Jekyll 使用

```bash
cd jekyll
cp _config.template.yaml _config.yaml
# 编辑 _config.yaml 填写实验室信息
bundle install
bundle exec jekyll serve
```

将 `index.template.md` 复制为 `index.md` 并按需修改。模板基于 Jekyll，可部署到 GitHub Pages。

---

## 3. 静态 HTML

将 `static/` 目录整体上传到任意静态托管（Nginx、Apache、对象存储等），访问 `index.html` 即可预览样式与布局。

适合作为其他 CMS（Hugo、Drupal 等）的 HTML/CSS 参考，将 `assets/css` 与 `assets/js` 引入即可复用样式。

---

## 资源说明

- **样式**：`assets/css/` 下为编译后的组件 CSS（与 Jekyll `_styles` 对应）。
- **脚本**：深色模式、中英文切换、搜索、表格等交互脚本位于 `assets/js/`。
- **图片**：仅包含模板占位图，不含实验室成员照片等站点专属内容。

## 许可证

遵循原 Lab Website Template 的 MIT 许可证。

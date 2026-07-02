#!/usr/bin/env python3
"""Export lab website template for WordPress, Jekyll, and static HTML."""

from __future__ import annotations

import json
import re
import shutil
import zipfile
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent
DIST = BASE / "dist" / "lab-website-template-export"
ZIP_PATH = BASE / "lab-website-template-export.zip"

THEME_SLUG = "lab-website-template"
CSS_ORDER = [
    "-theme.css",
    "alert.css",
    "all.css",
    "anchor.css",
    "background.css",
    "body.css",
    "bold.css",
    "button.css",
    "card.css",
    "checkbox.css",
    "citation.css",
    "code.css",
    "cols.css",
    "dark-toggle.css",
    "details.css",
    "feature.css",
    "figure.css",
    "float.css",
    "font.css",
    "footer.css",
    "form.css",
    "grid.css",
    "header.css",
    "heading.css",
    "highlight.css",
    "home.css",
    "icon.css",
    "image.css",
    "link.css",
    "list.css",
    "main.css",
    "paragraph.css",
    "portrait.css",
    "post-excerpt.css",
    "post-info.css",
    "post-nav.css",
    "quote.css",
    "rule.css",
    "search-box.css",
    "search-info.css",
    "section.css",
    "table.css",
    "tags.css",
    "textbox.css",
    "tooltip.css",
    "util.css",
]

TEMPLATE_IMAGES = [
    "background.jpg",
    "icon.png",
    "logo.svg",
    "share.jpg",
    "photo.jpg",
    "fallback.svg",
    "analysis.jpg",
    "testing.jpg",
    "ai.png",
    "students.jpg",
    "Papers.jpg",
    "automatic-generation-of-combinatorial-test-data.jpg",
    "logic-in-computer-science.jpg",
]

JEKYLL_COPY_DIRS = ["_layouts", "_includes", "_styles", "_scripts", "_plugins"]
JEKYLL_COPY_FILES = ["Gemfile", "Gemfile.lock", "404.md", "LICENSE.md"]
JEKYLL_SKIP_INCLUDES = {"analytics.html", "verification.html"}

STYLE_CSS = """/*
Theme Name: Lab Website Template
Theme URI: https://github.com/greenelab/lab-website-template
Author: Lab Website Template (adapted from Greene Lab)
Description: Academic lab website template with bilingual support, research cards, and publication layouts. Converted from the Jekyll Lab Website Template.
Version: 1.0.0
Requires at least: 6.0
Tested up to: 6.7
Requires PHP: 7.4
License: MIT
License URI: https://opensource.org/licenses/MIT
Text Domain: lab-website-template
Tags: education, custom-menu, translation-ready, one-column, custom-colors
*/

/* Component styles are loaded from assets/css/ via functions.php */
"""

FUNCTIONS_PHP = r"""<?php
/**
 * Lab Website Template functions.
 */

if (!defined('ABSPATH')) {
    exit;
}

define('LAB_THEME_VERSION', '1.0.0');

function lab_theme_setup(): void {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script']);

    register_nav_menus([
        'primary' => __('Primary Menu', 'lab-website-template'),
    ]);
}
add_action('after_setup_theme', 'lab_theme_setup');

function lab_theme_customize(WP_Customize_Manager $wp_customize): void {
    $wp_customize->add_section('lab_theme_options', [
        'title' => __('Lab Theme Options', 'lab-website-template'),
        'priority' => 30,
    ]);

    $wp_customize->add_setting('lab_site_email', [
        'default' => 'contact@example.com',
        'sanitize_callback' => 'sanitize_email',
    ]);
    $wp_customize->add_control('lab_site_email', [
        'label' => __('Contact Email', 'lab-website-template'),
        'section' => 'lab_theme_options',
        'type' => 'email',
    ]);

    $wp_customize->add_setting('lab_header_image', [
        'default' => get_template_directory_uri() . '/assets/images/background.jpg',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control(new WP_Customize_Image_Control($wp_customize, 'lab_header_image', [
        'label' => __('Header Background', 'lab-website-template'),
        'section' => 'lab_theme_options',
    ]));

    $wp_customize->add_setting('lab_footer_image', [
        'default' => get_template_directory_uri() . '/assets/images/background.jpg',
        'sanitize_callback' => 'esc_url_raw',
    ]);
    $wp_customize->add_control(new WP_Customize_Image_Control($wp_customize, 'lab_footer_image', [
        'label' => __('Footer Background', 'lab-website-template'),
        'section' => 'lab_theme_options',
    ]));
}
add_action('customize_register', 'lab_theme_customize');

function lab_theme_enqueue_assets(): void {
    $uri = get_template_directory_uri();
    $ver = LAB_THEME_VERSION;

    wp_enqueue_style(
        'lab-pygments',
        'https://cdn.jsdelivr.net/gh/StylishThemes/Syntax-Themes/pygments/css-github/pygments-tomorrow-night-eighties.css',
        [],
        null
    );
    wp_enqueue_style('lab-fonts', 'https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,200;0,400;0,500;0,600;1,200;1,400;1,500;1,600&family=Roboto+Mono:ital,wght@0,200;0,400;0,500;0,600&display=swap', [], null);
    wp_enqueue_style('lab-fontawesome', 'https://use.fontawesome.com/releases/v6.7.0/css/all.css', [], '6.7.0');

    $styles = lab_theme_css_files();
    $prev = ['lab-fontawesome'];
    foreach ($styles as $file) {
        $handle = 'lab-' . preg_replace('/[^a-z0-9]+/i', '-', $file);
        wp_enqueue_style($handle, $uri . '/assets/css/' . $file, $prev, $ver);
        $prev = [$handle];
    }

    wp_enqueue_script('lab-popper', 'https://unpkg.com/@popperjs/core@2', [], null, true);
    wp_enqueue_script('lab-tippy', 'https://unpkg.com/tippy.js@6', ['lab-popper'], null, true);
    wp_enqueue_script('lab-mark', 'https://unpkg.com/mark.js@8', [], null, true);

    foreach (lab_theme_js_files() as $file) {
        $handle = 'lab-' . pathinfo($file, PATHINFO_FILENAME);
        wp_enqueue_script($handle, $uri . '/assets/js/' . $file, [], $ver, true);
    }

    $i18n_path = get_template_directory() . '/assets/i18n.json';
    if (file_exists($i18n_path)) {
        $i18n = file_get_contents($i18n_path);
        wp_add_inline_script('lab-lang-toggle', 'window.I18N = ' . $i18n . ';', 'before');
    }
}
add_action('wp_enqueue_scripts', 'lab_theme_enqueue_assets');

function lab_theme_css_files(): array {
    return json_decode(file_get_contents(get_template_directory() . '/assets/css-order.json'), true) ?: [];
}

function lab_theme_js_files(): array {
    $dir = get_template_directory() . '/assets/js';
    if (!is_dir($dir)) {
        return [];
    }
    return array_values(array_filter(scandir($dir), static fn($f) => str_ends_with($f, '.js')));
}

function lab_theme_logo_html(): string {
    $svg = get_template_directory() . '/assets/images/logo.svg';
    if (file_exists($svg)) {
        return file_get_contents($svg);
    }
    $png = get_template_directory_uri() . '/assets/images/icon.png';
    return '<img src="' . esc_url($png) . '" alt="logo">';
}

function lab_theme_nav_fallback(): void {
    $pages = [
        'home' => home_url('/'),
        'team' => home_url('/team/'),
        'news' => home_url('/news/'),
        'publications' => home_url('/publications/'),
        'contact' => home_url('/contact/'),
    ];
    foreach ($pages as $key => $url) {
        printf(
            '<a href="%s" data-i18n="nav.%s">%s</a>',
            esc_url($url),
            esc_attr($key),
            esc_html($key)
        );
    }
}

function lab_theme_body_attributes(): string {
    $attrs = [
        'lang="zh"',
        'data-dark="false"',
        'data-lang="zh"',
        'data-i18n-page-title="' . esc_attr(get_post_meta(get_queried_object_id(), 'lab_i18n_title', true) ?: '') . '"',
        'data-i18n-site-title="site.title"',
        'data-i18n-description="' . esc_attr(get_post_meta(get_queried_object_id(), 'lab_i18n_description', true) ?: '') . '"',
        'data-page-title-fallback="' . esc_attr(wp_get_document_title()) . '"',
        'data-page-description-fallback="' . esc_attr(get_bloginfo('description')) . '"',
    ];
    return implode(' ', $attrs);
}
"""

HEADER_PHP = r"""<!DOCTYPE html>
<html <?php language_attributes(); ?> <?php echo lab_theme_body_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="<?php echo esc_url(get_template_directory_uri() . '/assets/images/icon.png'); ?>">
  <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<?php
$header_image = get_theme_mod('lab_header_image', get_template_directory_uri() . '/assets/images/background.jpg');
?>
<header class="background" style="--image: url('<?php echo esc_url($header_image); ?>')" data-dark="true">
  <a href="<?php echo esc_url(home_url('/')); ?>" class="home">
    <span class="logo"><?php echo lab_theme_logo_html(); ?></span>
    <span class="title-text" data-i18n-tooltip="nav.home_tooltip">
      <span class="title" data-i18n="site.title"><?php bloginfo('name'); ?></span>
      <span class="subtitle" data-i18n="site.subtitle"><?php bloginfo('description'); ?></span>
    </span>
  </a>
  <input class="nav-toggle" type="checkbox" data-i18n-aria="nav.toggle" aria-label="Toggle navigation">
  <nav>
    <?php
    wp_nav_menu([
        'theme_location' => 'primary',
        'container' => false,
        'items_wrap' => '%3$s',
        'fallback_cb' => 'lab_theme_nav_fallback',
    ]);
    ?>
  </nav>
</header>
<main>
"""

FOOTER_PHP = r"""</main>
<?php
$footer_image = get_theme_mod('lab_footer_image', get_template_directory_uri() . '/assets/images/background.jpg');
$email = get_theme_mod('lab_site_email', 'contact@example.com');
?>
<footer class="background" style="--image: url('<?php echo esc_url($footer_image); ?>')" data-dark="true" data-size="wide">
  <motioniv>
    Contact: <?php echo esc_html($email); ?>
  </div>
  <motioniv>
    &copy; <?php echo esc_html(gmdate('Y')); ?>
    <span data-i18n="site.title"><?php bloginfo('name'); ?></span>
  </div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
"""

# Fix typo motioniv -> div in footer
FOOTER_PHP = FOOTER_PHP.replace("<motioniv>", "<motioniv>").replace("</motioniv>", "</motioniv>")
FOOTER_PHP = FOOTER_PHP.replace("motioniv", "motioniv")
# I made a typo - let me fix properly
FOOTER_PHP = r"""</main>
<?php
$footer_image = get_theme_mod('lab_footer_image', get_template_directory_uri() . '/assets/images/background.jpg');
$email = get_theme_mod('lab_site_email', 'contact@example.com');
?>
<footer class="background" style="--image: url('<?php echo esc_url($footer_image); ?>')" data-dark="true" data-size="wide">
  <div>
    Contact: <?php echo esc_html($email); ?>
  </motioniv>
  <motioniv>
    &copy; <?php echo esc_html(gmdate('Y')); ?>
    <span data-i18n="site.title"><?php bloginfo('name'); ?></span>
  </motioniv>
</footer>
<?php wp_footer(); ?>
</body>
</html>
"""

# Still wrong - rewrite footer cleanly
FOOTER_PHP = """</main>
<?php
$footer_image = get_theme_mod('lab_footer_image', get_template_directory_uri() . '/assets/images/background.jpg');
$email = get_theme_mod('lab_site_email', 'contact@example.com');
?>
<footer class="background" style="--image: url('<?php echo esc_url($footer_image); ?>')" data-dark="true" data-size="wide">
  <div>
    Contact: <?php echo esc_html($email); ?>
  </div>
  <div>
    &copy; <?php echo esc_html(gmdate('Y')); ?>
    <span data-i18n="site.title"><?php bloginfo('name'); ?></span>
  </div>
</footer>
<?php wp_footer(); ?>
</body>
</html>
"""

INDEX_PHP = """<?php
/**
 * Main template – displays pages and posts.
 */
get_header();
if (have_posts()) {
    while (have_posts()) {
        the_post();
        echo '<section class="background" data-size="page">';
        echo '<h1>' . esc_html(get_the_title()) . '</h1>';
        the_content();
        echo '</section>';
    }
} else {
    echo '<section class="background" data-size="page"><p>' . esc_html__('No content found.', 'lab-website-template') . '</p></section>';
}
get_footer();
"""

PAGE_PHP = INDEX_PHP.replace('Main template', 'Page template')

SINGLE_PHP = """<?php
/**
 * Single post template.
 */
get_header();
while (have_posts()) {
    the_post();
    echo '<section class="background" data-size="page">';
    echo '<h1>' . esc_html(get_the_title()) . '</h1>';
    echo '<p class="post-info">' . esc_html(get_the_date()) . '</p>';
    the_content();
    echo '</section>';
}
get_footer();
"""

FRONT_PAGE_PHP = r"""<?php
/**
 * Front page demo – mirrors the Jekyll home layout.
 */
get_header();
$img = get_template_directory_uri() . '/assets/images';
?>
<section class="background" data-size="page">
  <h1 class="center" data-i18n="home.title">Welcome</h1>
  <p class="center" data-i18n="home.intro">Introduce your lab here.</p>
</section>

<section class="background" data-dark="true" data-size="page">
  <h2 class="center" data-i18n="home.research_title">Research Areas</h2>
  <motioniv class="cols" style="--cols: 3">
    <div class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/analysis.jpg" alt="Research 1" loading="lazy"></a>
      <div class="card-text">
        <a class="card-title" href="#">Program Analysis</a>
        <p>Describe your first research direction.</p>
      </div>
    </div>
    <div class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/testing.jpg" alt="Research 2" loading="lazy"></a>
      <motioniv class="card-text">
        <a class="card-title" href="#">Software Testing</a>
        <p>Describe your second research direction.</p>
      </motioniv>
    </motioniv>
    <motioniv class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/ai.png" alt="Research 3" loading="lazy"></a>
      <motioniv class="card-text">
        <a class="card-title" href="#">AI &amp; SE</a>
        <p>Describe your third research direction.</p>
      </motioniv>
    </motioniv>
  </motioniv>
</section>

<section class="background" data-size="page">
  <motioniv class="feature">
    <a class="feature-image" href="<?php echo esc_url(home_url('/team/')); ?>"><img src="<?php echo esc_url($img); ?>/students.jpg" alt="Team" loading="lazy"></a>
    <motioniv class="feature-text">
      <p class="feature-title" data-i18n="home.team_title">Team</p>
      <p>Introduce your team.</p>
      <a class="button" href="<?php echo esc_url(home_url('/team/')); ?>" data-i18n="home.team_button">Meet the team</a>
    </motioniv>
  </motioniv>
</section>

<section class="background" data-dark="true" data-size="page">
  <motioniv class="feature" data-flip>
    <a class="feature-image" href="<?php echo esc_url(home_url('/publications/')); ?>"><img src="<?php echo esc_url($img); ?>/Papers.jpg" alt="Publications" loading="lazy"></a>
    <motioniv class="feature-text">
      <p class="feature-title" data-i18n="home.projects_title">Publications</p>
      <p>Highlight representative papers and projects.</p>
      <a class="button" href="<?php echo esc_url(home_url('/publications/')); ?>" data-i18n="home.projects_button">View publications</a>
    </motioniv>
  </motioniv>
</section>

<section class="background" data-size="page">
  <h2 class="center" data-i18n="home.news_title">Latest News</h2>
  <ul>
    <li><strong>2026.01:</strong> Example news item – replace with your updates.</li>
  </ul>
</section>
<?php get_footer(); ?>
"""

# Fix motioniv typos in FRONT_PAGE_PHP
FRONT_PAGE_PHP = FRONT_PAGE_PHP.replace("motioniv", "motioniv")
FRONT_PAGE_PHP = FRONT_PAGE_PHP.replace("motioniv", "div")

PAGE_404_PHP = """<?php
/**
 * 404 template.
 */
get_header();
echo '<section class="background" data-size="page">';
echo '<h1 data-i18n="error.not_found">404</h1>';
echo '<p data-i18n="error.not_found_prompt">' . esc_html__('Page not found.', 'lab-website-template') . '</p>';
echo '</section>';
get_footer();
"""

README_MD = """# Lab Website Template Export

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
"""


def read_i18n_generic() -> dict:
    path = BASE / "_data" / "i18n.yaml"
    with open(path, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    # Use shorter generic intro for template distribution
    for lang in ("zh", "en"):
        if lang in data and "home" in data[lang]:
            data[lang]["home"]["intro"] = (
                "Introduce your research lab here. Replace this text in assets/i18n.json (WordPress) "
                "or _data/i18n.yaml (Jekyll)."
                if lang == "en"
                else "在此介绍您的研究室。请在 assets/i18n.json（WordPress）或 _data/i18n.yaml（Jekyll）中修改此文案。"
            )
        if lang in data and "site" in data[lang]:
            data[lang]["site"]["title"] = (
                "Lab Website Template" if lang == "en" else "实验室网站模板"
            )
    return data


def copy_compiled_css(dest: Path) -> list[str]:
    src_dir = BASE / "_site" / "_styles"
    if not src_dir.exists():
        src_dir = BASE / "_styles"
        raise SystemExit(
            "Compiled CSS not found. Run `bundle exec jekyll build` first, or ensure _site/_styles exists."
        )
    dest.mkdir(parents=True, exist_ok=True)
    copied = []
    for name in CSS_ORDER:
        src = src_dir / name
        if src.exists():
            shutil.copy2(src, dest / name)
            copied.append(name)
    # include any extra css not in order list
    for f in sorted(src_dir.glob("*.css")):
        if f.name.endswith(".map") or f.name in copied:
            continue
        shutil.copy2(f, dest / f.name)
        copied.append(f.name)
    return copied


def build_wordpress_theme(root: Path) -> None:
    theme = root / "wordpress" / THEME_SLUG
    theme.mkdir(parents=True, exist_ok=True)

    (theme / "style.css").write_text(STYLE_CSS, encoding="utf-8")
    (theme / "functions.php").write_text(FUNCTIONS_PHP, encoding="utf-8")
    (theme / "header.php").write_text(HEADER_PHP, encoding="utf-8")
    (theme / "footer.php").write_text(FOOTER_PHP, encoding="utf-8")
    (theme / "index.php").write_text(INDEX_PHP, encoding="utf-8")
    (theme / "page.php").write_text(PAGE_PHP, encoding="utf-8")
    (theme / "single.php").write_text(SINGLE_PHP, encoding="utf-8")
    (theme / "front-page.php").write_text(FRONT_PAGE_PHP, encoding="utf-8")
    (theme / "404.php").write_text(PAGE_404_PHP, encoding="utf-8")

    css_dest = theme / "assets" / "css"
    css_files = copy_compiled_css(css_dest)
    (theme / "assets" / "css-order.json").write_text(
        json.dumps(css_files, indent=2), encoding="utf-8"
    )

    js_src = BASE / "_scripts"
    js_dest = theme / "assets" / "js"
    js_dest.mkdir(parents=True, exist_ok=True)
    for f in js_src.glob("*.js"):
        shutil.copy2(f, js_dest / f.name)

    img_dest = theme / "assets" / "images"
    img_dest.mkdir(parents=True, exist_ok=True)
    for name in TEMPLATE_IMAGES:
        src = BASE / "images" / name
        if src.exists():
            shutil.copy2(src, img_dest / name)

    i18n = read_i18n_generic()
    (theme / "assets" / "i18n.json").write_text(
        json.dumps(i18n, ensure_ascii=False, indent=2), encoding="utf-8"
    )

  # screenshot for WP theme directory
    icon = BASE / "images" / "share.jpg"
    if icon.exists():
        shutil.copy2(icon, theme / "screenshot.png")


def build_jekyll_template(root: Path) -> None:
    jekyll = root / "jekyll"
    jekyll.mkdir(parents=True, exist_ok=True)

    for d in JEKYLL_COPY_DIRS:
        src = BASE / d
        if not src.exists():
            continue
        dest = jekyll / d
        if dest.exists():
            shutil.rmtree(dest)
        if d == "_includes":
            dest.mkdir(parents=True)
            for f in src.iterdir():
                if f.name in JEKYLL_SKIP_INCLUDES:
                    continue
                if f.is_file():
                    shutil.copy2(f, dest / f.name)
        else:
            shutil.copytree(src, dest)

    for f in JEKYLL_COPY_FILES:
        src = BASE / f
        if src.exists():
            shutil.copy2(src, jekyll / f)

    config = {
        "title": "Lab Website Template",
        "subtitle": "",
        "description": "An academic lab website built with the Lab Website Template.",
        "header": "images/background.jpg",
        "footer": "images/background.jpg",
        "links": {"email": "contact@example.com"},
        "defaults": [
            {"scope": {"path": ""}, "values": {"layout": "default"}},
            {"scope": {"type": "members"}, "values": {"layout": "member"}},
            {"scope": {"type": "posts"}, "values": {"layout": "post"}},
        ],
        "collections": {
            "members": {"output": True},
            "posts": {"output": True},
        },
        "plugins": [
            "jekyll-spaceship",
            "jekyll-sitemap",
            "jekyll-redirect-from",
            "jekyll-feed",
            "jekyll-last-modified-at",
        ],
        "highlighter": "rouge",
        "theme": None,
        "sass": {"sass_dir": "_styles"},
        "include": ["_styles", "_scripts"],
        "exclude": ["README.md", "LICENSE.md"],
    }
    with open(jekyll / "_config.template.yaml", "w", encoding="utf-8") as f:
        yaml.dump(config, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    data_dir = jekyll / "_data"
    data_dir.mkdir(exist_ok=True)
    with open(data_dir / "i18n.yaml", "w", encoding="utf-8") as f:
        yaml.dump(read_i18n_generic(), f, allow_unicode=True, default_flow_style=False, sort_keys=False)

    for name in ("projects.yaml", "sources.yaml", "types.yaml", "orcid.yaml"):
        src = BASE / "_data" / name
        if src.exists():
            shutil.copy2(src, data_dir / name)

    img_dir = jekyll / "images"
    img_dir.mkdir(exist_ok=True)
    for name in TEMPLATE_IMAGES:
        src = BASE / "images" / name
        if src.exists():
            shutil.copy2(src, img_dir / name)

    index_template = """---
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
"""
    (jekyll / "index.template.md").write_text(index_template, encoding="utf-8")

    (jekyll / "README.md").write_text(
        "# Jekyll Lab Website Template\n\nCopy `_config.template.yaml` to `_config.yaml`, "
        "`index.template.md` to `index.md`, then run `bundle install && bundle exec jekyll serve`.\n",
        encoding="utf-8",
    )


def build_static_demo(root: Path) -> None:
    static = root / "static"
    assets = static / "assets"
    css_dest = assets / "css"
    copy_compiled_css(css_dest)

    js_dest = assets / "js"
    js_dest.mkdir(parents=True, exist_ok=True)
    for f in (BASE / "_scripts").glob("*.js"):
        shutil.copy2(f, js_dest / f.name)

    img_dest = assets / "images"
    img_dest.mkdir(parents=True, exist_ok=True)
    for name in TEMPLATE_IMAGES:
        src = BASE / "images" / name
        if src.exists():
            shutil.copy2(src, img_dest / name)

    i18n = read_i18n_generic()
    i18n_script = f"<script>window.I18N = {json.dumps(i18n, ensure_ascii=False)};</script>"

    css_links = "\n".join(
        f'  <link href="assets/css/{name}" rel="stylesheet">' for name in CSS_ORDER
        if (css_dest / name).exists()
    )
    js_scripts = "\n".join(
        f'  <script src="assets/js/{f.name}" defer></script>'
        for f in sorted(js_dest.glob("*.js"))
    )

    img = "assets/images"
    html = f"""<!DOCTYPE html>
<html lang="zh" data-dark="false" data-lang="zh" data-i18n-page-title="home.title" data-i18n-site-title="site.title" data-i18n-description="home.intro">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Lab Website Template</title>
  <link rel="icon" href="{img}/icon.png">
  <link href="https://fonts.googleapis.com/css2?family=Barlow:wght@200;400;500;600&family=Roboto+Mono:wght@400&display=swap" rel="stylesheet">
  <link href="https://use.fontawesome.com/releases/v6.7.0/css/all.css" rel="stylesheet">
{css_links}
  {i18n_script}
</head>
<body>
<header class="background" style="--image: url('{img}/background.jpg')" data-dark="true">
  <a href="index.html" class="home">
    <span class="logo"><img src="{img}/icon.png" alt="logo" style="height:48px"></span>
    <span class="title-text"><span class="title" data-i18n="site.title">Lab</span></span>
  </a>
  <input class="nav-toggle" type="checkbox" aria-label="Menu">
  <nav>
    <a href="index.html" data-i18n="nav.home">Home</a>
    <a href="#team" data-i18n="nav.team">Team</a>
    <a href="#news" data-i18n="nav.news">News</a>
    <a href="#publications" data-i18n="nav.publications">Publications</a>
    <a href="#contact" data-i18n="nav.contact">Contact</a>
  </nav>
</header>
<main>
<section class="background" data-size="page">
  <h1 class="center" data-i18n="home.title">Welcome</h1>
  <p class="center" data-i18n="home.intro">Introduce your lab.</p>
</section>
<section class="background" data-dark="true" data-size="page">
  <h2 class="center" data-i18n="home.research_title">Research</h2>
  <motioniv class="cols" style="--cols:3">
    <motioniv class="card"><a class="card-image" href="#"><img src="{img}/analysis.jpg" alt=""></a><motioniv class="card-text"><a class="card-title" href="#">Area 1</a><p>Description.</p></motioniv></motioniv>
    <motioniv class="card"><a class="card-image" href="#"><img src="{img}/testing.jpg" alt=""></a><motioniv class="card-text"><a class="card-title" href="#">Area 2</a><p>Description.</p></motioniv></motioniv>
    <motioniv class="card"><a class="card-image" href="#"><img src="{img}/ai.png" alt=""></a><motioniv class="card-text"><a class="card-title" href="#">Area 3</a><p>Description.</p></motioniv></motioniv>
  </motioniv>
</section>
<section class="background" data-size="page" id="news">
  <h2 class="center" data-i18n="home.news_title">News</h2>
  <ul><li><strong>2026.01:</strong> Example news.</li></ul>
</section>
</main>
<footer class="background" style="--image: url('{img}/background.jpg')" data-dark="true" data-size="wide">
  <div id="contact">Contact: contact@example.com</div>
  <div>&copy; 2026 <span data-i18n="site.title">Lab</span></div>
</footer>
{js_scripts}
</body>
</html>
"""
    html = html.replace("motioniv", "div")
    (static / "index.html").write_text(html, encoding="utf-8")


def create_wp_upload_zip(theme_dir: Path, zip_path: Path) -> None:
    """Separate zip with theme folder at root for WP upload."""
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in theme_dir.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(theme_dir.parent))


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    build_wordpress_theme(DIST)
    build_jekyll_template(DIST)
    build_static_demo(DIST)
    (DIST / "README.md").write_text(README_MD, encoding="utf-8")

    # Full export archive
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()
    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in DIST.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(DIST.parent))

    # WordPress-only upload zip
    wp_zip = BASE / f"{THEME_SLUG}-wordpress.zip"
    if wp_zip.exists():
        wp_zip.unlink()
    create_wp_upload_zip(DIST / "wordpress" / THEME_SLUG, wp_zip)

    theme_dir = DIST / "wordpress" / THEME_SLUG
    print(f"Export complete:")
    print(f"  Full package: {ZIP_PATH} ({ZIP_PATH.stat().st_size // 1024} KB)")
    print(f"  WordPress upload: {wp_zip} ({wp_zip.stat().st_size // 1024} KB)")
    print(f"  Extracted: {DIST}")


if __name__ == "__main__":
    main()

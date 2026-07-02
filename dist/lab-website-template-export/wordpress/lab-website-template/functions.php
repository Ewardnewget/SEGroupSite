<?php
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

<!DOCTYPE html>
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

</main>
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

<?php
/**
 * 404 template.
 */
get_header();
echo '<section class="background" data-size="page">';
echo '<h1 data-i18n="error.not_found">404</h1>';
echo '<p data-i18n="error.not_found_prompt">' . esc_html__('Page not found.', 'lab-website-template') . '</p>';
echo '</section>';
get_footer();

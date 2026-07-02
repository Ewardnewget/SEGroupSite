<?php
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

<?php
/**
 * Page template – displays pages and posts.
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

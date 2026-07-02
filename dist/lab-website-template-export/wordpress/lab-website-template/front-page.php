<?php
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
  <div class="cols" style="--cols: 3">
    <div class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/analysis.jpg" alt="Research 1" loading="lazy"></a>
      <div class="card-text">
        <a class="card-title" href="#">Program Analysis</a>
        <p>Describe your first research direction.</p>
      </div>
    </div>
    <div class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/testing.jpg" alt="Research 2" loading="lazy"></a>
      <div class="card-text">
        <a class="card-title" href="#">Software Testing</a>
        <p>Describe your second research direction.</p>
      </div>
    </div>
    <div class="card">
      <a class="card-image" href="#"><img src="<?php echo esc_url($img); ?>/ai.png" alt="Research 3" loading="lazy"></a>
      <div class="card-text">
        <a class="card-title" href="#">AI &amp; SE</a>
        <p>Describe your third research direction.</p>
      </div>
    </div>
  </div>
</section>

<section class="background" data-size="page">
  <div class="feature">
    <a class="feature-image" href="<?php echo esc_url(home_url('/team/')); ?>"><img src="<?php echo esc_url($img); ?>/students.jpg" alt="Team" loading="lazy"></a>
    <div class="feature-text">
      <p class="feature-title" data-i18n="home.team_title">Team</p>
      <p>Introduce your team.</p>
      <a class="button" href="<?php echo esc_url(home_url('/team/')); ?>" data-i18n="home.team_button">Meet the team</a>
    </div>
  </div>
</section>

<section class="background" data-dark="true" data-size="page">
  <div class="feature" data-flip>
    <a class="feature-image" href="<?php echo esc_url(home_url('/publications/')); ?>"><img src="<?php echo esc_url($img); ?>/Papers.jpg" alt="Publications" loading="lazy"></a>
    <div class="feature-text">
      <p class="feature-title" data-i18n="home.projects_title">Publications</p>
      <p>Highlight representative papers and projects.</p>
      <a class="button" href="<?php echo esc_url(home_url('/publications/')); ?>" data-i18n="home.projects_button">View publications</a>
    </div>
  </div>
</section>

<section class="background" data-size="page">
  <h2 class="center" data-i18n="home.news_title">Latest News</h2>
  <ul>
    <li><strong>2026.01:</strong> Example news item – replace with your updates.</li>
  </ul>
</section>
<?php get_footer(); ?>

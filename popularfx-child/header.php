<?php
/**
 * The header for our theme
 *
 * This is the template that displays all of the <head> section and everything up until <div id="content">
 *
 * @link https://developer.wordpress.org/themes/basics/template-files/#template-partials
 *
 * @package PopularFX
 */
?>
<!doctype html>
<html <?php language_attributes(); ?>>
<head>
    <meta charset="<?php bloginfo( 'charset' ); ?>">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="profile" href="https://gmpg.org/xfn/11">
    <?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>
<div id="page" class="site">
    <a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e( 'Skip to content', 'popularfx' ); ?></a>
    <header id="masthead" class="site-header">
        <div class="site-branding">
            <?php
            the_custom_logo();
            if ( is_front_page() && is_home() ) :
                ?>
                <h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
                <?php
            else :
                ?>
                <p class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></p>
                <?php
            endif;
            $popularfx_description = get_bloginfo( 'description', 'display' );
            if ( $popularfx_description || is_customize_preview() ) :
                ?>
                <p class="site-description"><?php echo $popularfx_description; // phpcs:ignore WordPress.Security.EscapeOutput.OutputNotEscaped ?></p>
            <?php endif; ?>
        </div><!-- .site-branding -->
        <button class="menu-toggle" aria-controls="primary-menu" aria-expanded="false"><span class="dashicons dashicons-menu-alt2"></span></button>

        <button id="hamburger-menu" class="hamburger">☰</button>
        <nav id="mobile-menu" class="hidden">
        <ul>
            <li><a href="https://news-and-books.com/">Home</a></li>
            <li><a href="https://news-and-books.com/business/">Business</a></li>
            <li><a href="https://news-and-books.com/economy/">Economy</a></li>
            <li><a href="https://news-and-books.com/finance/">Finance</a></li>
            <li><a href="https://news-and-books.com/health/">Health</a></li>
            <li><a href="https://news-and-books.com/science/">Science</a></li>
            <li><a href="https://news-and-books.com/self-improvement/">Self Improvement</a></li>
            <li><a href="https://news-and-books.com/tech/">Technology</a></li>
            <li><a href="https://news-and-books.com/tech/ai/">AI</a></li>
            <li><a href="https://news-and-books.com/sg/">Singapore</a></li>
            <li><a href="https://news-and-books.com/jobs/">Jobs</a></li>
            <li><a href="https://news-and-books.com/books/">Books</a></li>
            <li><a href="https://news-and-books.com/newsletters/">Newsletters</a></li>
            <li><a href="https://news-and-books.com/affiliate-disclosure/">Affiliate Disclosure</a></li>
        </ul>
        </nav>
        <nav id="site-navigation" class="main-navigation hidden-mobile">

            <?php
            wp_nav_menu(
                array(
                    'theme_location' => 'primary',
                    'menu_id'        => 'primary-menu',
                )
            );
            ?>
        </nav><!-- #site-navigation -->
    </header><!-- #masthead -->
	
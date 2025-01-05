<?php
define( 'WP_CACHE', true );
 // Added by SpeedyCache

/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'newsdadw_wp2025db' );

/** Database username */
define( 'DB_USER', 'newsdadw_wp2025db' );

/** Database password */
define( 'DB_PASSWORD', '@2EuD[.s6!-pqD2S' );

/** Database hostname */
define( 'DB_HOST', 'localhost' );

/** Database charset to use in creating database tables. */
define( 'DB_CHARSET', 'utf8mb4' );

/** The database collate type. Don't change this if in doubt. */
define( 'DB_COLLATE', '' );

/**#@+
 * Authentication unique keys and salts.
 *
 * Change these to different unique phrases! You can generate these using
 * the {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}.
 *
 * You can change these at any point in time to invalidate all existing cookies.
 * This will force all users to have to log in again.
 *
 * @since 2.6.0
 */
define( 'AUTH_KEY',         'jvdqnbpl3z33x50x1l4hwwgshx3yy66h0qbwk0tljzvvxfxfes5q6jnansfdriwu' );
define( 'SECURE_AUTH_KEY',  'crhiqctlks4jwqy4ybu1tqyk4r1lvlgj8okyee9h2apozvcyeibfhpypwmltkdui' );
define( 'LOGGED_IN_KEY',    'wsbul0dka6dkemagzqgz5rgm3gq6rjmrpmwitsal8sgxb9n7ubgdpxe0og5njjnk' );
define( 'NONCE_KEY',        '9roo65kyxjy3gq7sicvgksedm6trp5xqzuwmllaiowwxwyvmsqfcstec9fp8lnj7' );
define( 'AUTH_SALT',        't2gdbmkyq3vsmy5xvdcqfyqqt9udgdxwlnmm8rhgsrpwhiozevnmcrfqowvoxiqp' );
define( 'SECURE_AUTH_SALT', 'l3psmfjbr07soeslj88re6b7iqqme63gycyuigjsdaf7zxasyjl0pzxb7k2tnyrk' );
define( 'LOGGED_IN_SALT',   'oavxib6nmdpwytvj2hwazaayargcefbqpx7reorcp1wg1arzhpd3ei5inqn00dsq' );
define( 'NONCE_SALT',       '5rcewog8p3iqskiobzay9u0y7ubx7hzuqzztsuinyg475y834njeuqcmtzeqjbfb' );

/**#@-*/

/**
 * WordPress database table prefix.
 *
 * You can have multiple installations in one database if you give each
 * a unique prefix. Only numbers, letters, and underscores please!
 *
 * At the installation time, database tables are created with the specified prefix.
 * Changing this value after WordPress is installed will make your site think
 * it has not been installed.
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/#table-prefix
 */
$table_prefix = 'wp2025_';

/**
 * For developers: WordPress debugging mode.
 *
 * Change this to true to enable the display of notices during development.
 * It is strongly recommended that plugin and theme developers use WP_DEBUG
 * in their development environments.
 *
 * For information on other constants that can be used for debugging,
 * visit the documentation.
 *
 * @link https://developer.wordpress.org/advanced-administration/debug/debug-wordpress/
 */
define( 'WP_DEBUG', true );
define( 'WP_DEBUG_LOG', true );
define('WP_DEBUG_DISPLAY', false);

/* Add any custom values between this line and the "stop editing" line. */

/* That's all, stop editing! Happy publishing. */

/** Absolute path to the WordPress directory. */
if ( ! defined( 'ABSPATH' ) ) {
	define( 'ABSPATH', __DIR__ . '/' );
}

/** Sets up WordPress vars and included files. */
require_once ABSPATH . 'wp-settings.php';

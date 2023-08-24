# fix error 500
exec { 'fix-php-500':
  command  => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path     => ['/usr/bin', '/bin'],
  returns  => [0, 1],
}

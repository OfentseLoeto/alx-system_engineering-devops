#Using strace, find out why Apache is returning a 500 error. 

class apache_fix {
 exec { 'restart_apache':
   command     => '/bin/sed -i s/class-wp-locale.phpp/class-wp-locale.php/g /var/www/html/wp-settings.php',
   refreshonly => true,
   require   => File['/var/www/html/wp-settings.php'],
}
}

class { 'apache_fix':}

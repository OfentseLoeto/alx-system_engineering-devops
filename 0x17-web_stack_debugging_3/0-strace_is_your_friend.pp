# This Puppet manifest fixes a PHP file reference issue in wp-settings.php
# and ensures the Apache service is restarted after the fix.

class apache_fix {
 # Ensure Apache2 package is installed
 package { 'apache2':
 ensure        => installed,
}

 # Copy the correct wp-settings.php file
file { '/var/www/html/wp-settings.php':
 ensure        => file,
 source        => '/var/www/html/wp-settings.php',
 mode          => '0644',
 require       => Package['apache2'],
 notify        => Exec['fix-php-500'],
}

 # Fix the PHP file reference issue
exec { 'fix-php-500':
 command       => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
 path          => ['/usr/bin', '/bin'],
 returns       => [0, 1],
 require       => File['/var/www/html/wp-settings.php'],
 notify        => Exec['restart_apache'],
}

 # Restart Apache service
exec { 'restart_apache':
 command       => '/usr/sbin/service apache2 restart',
 refreshonly   => true,
 subscribe     => File['/var/www/html/wp-settings.php'],
 require       => Package['apache2'],
  }
}

# Apply the apache_fix class
class { 'apache_fix': }

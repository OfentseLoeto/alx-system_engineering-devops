# Fix error 500
class apache_fix {
 package { 'apache2':
 ensure => installed,
}

file { '/var/www/html/wp-settings.php':
 ensure  => file,
 source  => 'puppet:///modules/apache_fix/wp-settings.php',
 mode    => '0644',
 require => Package['apache2'],
 notify  => Exec['fix-php-500'],
}

exec { 'fix-php-500':
 command     => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
 path        => ['/usr/bin', '/bin'],
 returns     => [0, 1],
 require     => File['/var/www/html/wp-settings.php'],
 notify      => Exec['restart_apache'],
}

exec { 'restart_apache':
 command     => '/usr/sbin/service apache2 restart',
 refreshonly => true,
 subscribe   => File['/var/www/html/wp-settings.php'],
 require     => Package['apache2'],
}
}

class { 'apache_fix': }

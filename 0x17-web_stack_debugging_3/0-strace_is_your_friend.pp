#Using strace, find out why Apache is returning a 500 error. 

class apache_fix {
  file { '/var/www/html/wp-settings.php':
    ensure  => file,
    source  => 'puppet:///modules/apache_fix/wp-settings.php',
    mode    => '0644',
    require => Package['apache2'],
    notify  => Exec['restart_apache'],
  }

  exec { 'restart_apache':
    command     => '/usr/sbin/service apache2 restart',
    refreshonly => true,
  }
}

class { 'apache_fix': }


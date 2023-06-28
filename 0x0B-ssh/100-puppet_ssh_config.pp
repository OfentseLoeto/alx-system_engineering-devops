file { '/root/ubuntu/.ssh/config':
  ensure => file,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  content => "
    Host 52.3.220.1
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}


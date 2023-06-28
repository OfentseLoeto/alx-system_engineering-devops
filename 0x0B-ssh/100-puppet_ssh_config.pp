# Script that configure client SSH configuration file
# using Puppet to use the private key 

file { '/home/0x0B-ssh/.ssh/config':
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


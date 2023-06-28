# Puppet manifest to install Flask version 2.1.0 from pip3

package { 'python3-pip':
  ensure => installed,
}


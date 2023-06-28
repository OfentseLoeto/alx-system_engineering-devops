# Puppet manifest to kill a process named "killmenow"

exec { 'kill_process':
  command => 'pkill killmenow',
  path    => '/usr/bin',
  onlyif  => 'pgrep killmenow',
}


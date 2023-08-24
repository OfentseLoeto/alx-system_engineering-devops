#Using strace, find out why Apache is returning error 500

exec { 'fix-php-500':
   environment => ['DIR=/var/www/html/wp-settings.phpp',
                  'OLD=phpp',
                  'NEW=php'],
   command    => 'sudo sed -i "s/$OLD/$NEW/" $DIR',
   path       => ['/usr/bin', '/bin'],
   returns    => [0, 1]
}

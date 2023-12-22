# kills killmenow

exec { 'killmenow':
  command   => '/usr/bin/pkill -TERM killmenow',
}

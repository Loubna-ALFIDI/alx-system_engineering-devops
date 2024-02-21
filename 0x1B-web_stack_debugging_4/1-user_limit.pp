# update soft limit
# Change the OS configuration so that it is possible to login with the holberton user and open a file without any error message.
exec { 'update soft limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'update hard limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}

# Client configuration file (w/ Puppet)

file_line { "Turn off passwd auth":
    ensure => present,
    path => "/etc/ssh/ssh_config",
    line => "PasswordAuthentification no",
}

file_line { "Declare identify file":
    path => "/etc/ssh/ssh_config",
    line => "IdentityFile ~/.ssh/school",
}

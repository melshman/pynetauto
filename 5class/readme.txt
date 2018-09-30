must put the eapi.conf file in the home directory

~/.eapi.conf

here is the contents of the file for the ntc lab

 [connection:pynet-sw4]
 host: 184.105.247.75
 
 [connection:pynet-sw3]
 host: 184.105.247.74
 
 [DEFAULT]
 transport: https
 username: pyclass
 password: 88newclass

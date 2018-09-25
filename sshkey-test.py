#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

pub_key = "/home/tarmstrong/.ssh/test_sshkey.pub"
# pub_key = "/home/melshman/.ssh/id_rsa.pub"
# password = getpass()

VTswitch = {
    'device_type': 'cisco_ios',
    'host': '192.168.2.101', 
    'username': 'admin',
    'use_keys': True,
    'key_file': pub_key,
}

pynet_rtr1  = {
    'device_type': 'cisco_ios',
    'host': '184.105.247.70', 
    'username': 'pyclass',
    'use_keys': True,
    'key_file': pub_key,
    # 'password' = password
}


# net_connect = Netmiko(**VTswitch)

net_connect = Netmiko(**pynet_rtr1)
print(net_connect.find_prompt())
output = net_connect.send_command("show version")
print(output)
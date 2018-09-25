#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass

pub_key = "/home/melshman/.ssh/id_rsa.pub"

VTswitch = {
    'device_type': 'cisco_ios',
    'host': '192.168.2.101', 
    'username': 'admin',
    'use_keys': True,
    'key_file': pub_key,
}

net_connect = Netmiko(**VTswitch)
print(net_connect.find_prompt())
output = net_connect.send_command("show version")
print(output)
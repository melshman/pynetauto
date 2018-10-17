#!/usr/bin/env python


"""
7. Use the pynxos library to configure a loopback interface on nxos1. Choose a random loopback interface number 
between 1 and 99. Assign the loopback interface an IP address in the 172.16.0.0 - 172.31.255.255. Use a /32 netmask.

Execute a 'show run interface loopbackX' command using NX-API to verify your interface was configured properly. For example:

-----------
nxapi_conn.show('show run interface loopback99', raw_text=True)
-----------
Note, you will need to use 'raw_text=True' for this command.
"""


from __future__ import unicode_literals, print_function
from pynxos.device import Device
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint


def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    hosts = ['nxos1.twb-tech.com', 'nxos2.twb-tech.com']
    password = getpass()
    command_list = ['interface Loopback66', 'ip address 172.31.255.66/32']

    for host in hosts:
	    device = Device(host=host,
	    	username='pyclass',
	    	password=password,
	    	transport='https',
	    	port=8443)
	    device.config_list(command_list)
	    result = device.show('show run interface loopback66', raw_text=True)
	    print(result)

if __name__ == '__main__':
    main()


# interface Loopback66
#  ip address {{loopback_vars.loopback0_addr}} {{loopback_vars.loopback0_mask}}

#############    help(device) ##################
# class Device(builtins.object)
#  |  Methods defined here:
#  |
#  |  __init__(self, host, username, password, transport='http', port=None, timeout=30)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  backup_running_config(self, filename)
#  |
#  |  checkpoint(self, filename)
#  |
#  |  config(self, command)
#  |
#  |  config_list(self, commands)
#  |
#  |  feature(self, feature_name)
#  |
#  |  file_copy(self, src, dest=None, file_system='bootflash:')
#  |
#  |  file_copy_remote_exists(self, src, dest=None, file_system='bootflash:')
#  |
#  |  get_boot_options(self)
#  |
#  |  reboot(self, confirm=False)
#  |
#  |  rollback(self, filename)
#  |
#  |  save(self, filename='startup-config')
#  |
#  |  set_boot_options(self, image_name, kickstart=None)
#  |
#  |  show(self, command, raw_text=False)
#  |
#  |  show_list(self, commands, raw_text=False)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  facts
#  |
#  |  running_config
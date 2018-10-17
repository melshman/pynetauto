#!/usr/bin/env python


"""
6. Use the pynxos library and NX-API to retrieve the output of 
'show ip route vrf management' from the nxos1 switch. 
Parse the returned data structure and from this, retrieve the 
next hop for the default route. Print this to standard output.
"""


from __future__ import unicode_literals, print_function
# from jinja2 import FileSystemLoader, StrictUndefined
# from jinja2.environment import Environment
from pynxos.device import Device
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint


def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	for host in ['nxos1.twb-tech.com', 'nxos2.twb-tech.com']:
	    device = Device(host=host,
	    	username='pyclass',
	    	password=getpass(),
	    	transport='https',
	    	port=8443)
	    result = device.show('show ip route vrf management')
	    # ipnexthop = result['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix'][0]['TABLE_path']['ROW_path']['ipnexthop']
	    route_table = result['TABLE_vrf']['ROW_vrf']['TABLE_addrf']['ROW_addrf']['TABLE_prefix']['ROW_prefix']
	    print(host)
	    print('-' * 40)
	    print(route_table)
	    print('-' * 40)

	    for route_entry in route_table:
	        if route_entry['ipprefix'] == '0.0.0.0/0':
	            next_hop = route_entry['TABLE_path']['ROW_path']['ipnexthop'] 
	            print("Default Gateway: {}".format(next_hop))
	            break
	    print('-' * 40)


if __name__ == '__main__':
    main()

# interface Loopback0
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
#!/user/bin/env python

from __future__ import print_function, unicode_literals

from getpass import getpass
from pprint import pprint

from netmiko import ConnectHandler


"""

4. Use Netmiko and TextFSM to retrieve 'show ip int brief' from pynet-rtr2 as 
structured data.

This will require that you install ntc-templates into the lab environment as follows:
# cd to the base of your home directory
$ cd ~

# Git clone ntc-templates into this directory
$ git clone https://github.com/networktocode/ntc-templates

# At the end of this you should have ntc-templates on this path
$ ls ~/ntc-templates/templates/index

In order to do this, besides adding ntc-templates into the above path, you 
will also need to add the 'use_textfsm=True' argument when calling the send_command() method.

Note, if your TextFSM lookup fails, you will probably get unstructured data 
returned to you. You can also set this environment variable (if your TextFSM lookup is failing).
$ export NET_TEXTFSM=/path/to/ntc-templates/templates/

After you have retrieved this 'show ip int brief' output as structured data. 
Parse the returned data structure and print out the IP address associated with FastEthernet4.


"""

def main():
	password = getpass()

	VTswitch = { 
	    'device_type': 'cisco_ios',
	    'host': '192.168.2.101',
	    'username': 'admin',
	    'password': password,
	    'file_system': 'flash:'
	    }

	switch07 = { 
	    'device_type': 'cisco_ios',
	    'host': '192.168.2.7',
	    'username': 'admin',
	    'password': password,
	    'file_system': 'flash:'
	    }

	pynet_rtr2 = { 
	    'device_type': 'cisco_ios',
	    'host': '184.105.247.71',
	    'username': 'pyclass',
	    'password': password,
	    'file_system': '/mnt/flash'
	    }

	# for a_device in (pynet_rtr2,):  # use with pynet AWS lab environment
	for a_device in (VTswitch, ):     # use with ctil lab environment
		"""Execute show ip int brief command using Netmiko."""
		remote_conn = ConnectHandler(device_type=a_device['device_type'],
	                             ip=a_device['host'],
	                             username=a_device['username'],
	                             password=a_device['password'])
		print()
		print('#' * 80)
		ip_int_brief = remote_conn.send_command("show ip int brief", use_textfsm=True)
		# pprint(remote_conn.send_command("show ip int brief"))
		pprint(ip_int_brief)
		print("The IP Address of interface VLAN 1 is {}".format(ip_int_brief[0]['ipaddr']))
		print('#' * 80)
		print()
		remote_conn.disconnect()


if __name__ == "__main__":
	main()

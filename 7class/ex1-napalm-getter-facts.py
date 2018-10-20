#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from napalm import get_network_driver

"""

1. Construct a script that retrieves NAPALM facts from two IOS routers, two Arista switches, 
one Junos device, and one NX-OS switch.
pynet-rtr1   (Cisco IOS)  184.105.247.70
pynet-rtr2   (Cisco IOS)  184.105.247.71
pynet-sw1    (Arista EOS) 184.105.247.72
pynet-sw2    (Arista EOS) 184.105.247.73
​juniper-srx               184.105.247.76
nxos1        (Cisco NXOS) nxos1.twb-tech.com

Retrieve the 'model' number from each device and print the model to standard out.

As part of this exercise define the devices that you use in a Python file 
(for example my_devices.py) and import these devices into your program. 
Optionally, define the devices in a YAML file and read this my_devices.yml 
file into your program.

Note, NAPALM will automatically make a connection using the appropriate transport 
as part of this exercise. The transports will be as follows 
(Cisco IOS = SSH, Arista EOS = eAPI, Juniper = NETCONF, Cisco NX-OS = NX-API).

"""


def main():
	password = getpass()

	cisco_rtr1 = {
		'hostname' : '184.105.247.70',
		'device_type' : 'ios',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	cisco_rtr2 = {
		'hostname' : '184.105.247.71',
		'device_type' : 'ios',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	arista_sw1 = {
		'hostname' : '184.105.247.72',
		'device_type' : 'eos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	arista_sw2 = {
		'hostname' : '184.105.247.73',
		'device_type' : 'eos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}

	jnpr_srx1 = {
		'hostname' : '184.105.247.76',
		'device_type' : 'junos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	cisco_nxos = {
		'hostname' : 'nxos1.twb-tech.com',
		'device_type' : 'nxos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}


	devices = (cisco_rtr1, cisco_rtr2, arista_sw1, arista_sw2, jnpr_srx1, cisco_nxos)


	for a_device in devices:
		device_type = a_device.pop('device_type')
		driver = get_network_driver(device_type)
		device = driver(**a_device)
		napalm_conns.append(device)
		print("\n {} device created!".format(hostname))
		device.open()
		print("\n Device connection opened of type {}!".format(device_type))
		print("\n\n")
		facts = device.get_facts()
		pprint(facts)
		print("\n\n")


if __name__ == "__main__":
	main()


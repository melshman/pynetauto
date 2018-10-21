#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from napalm import get_network_driver
# from my_devices import devices
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

"""

2. Using NAPALM retrieve 'get_lldp_neighbors' from pynet-rtr1 and from 
pynet-rtr2. Print out retrieved LLDP information to standard output.

"""

def main():
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
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
		'optional_args' : {'port' : '8443',
							'nxos_protocol' : 'https'
		}
	}


	# devices = (cisco_rtr1, cisco_rtr2, arista_sw1, arista_sw2, jnpr_srx1, cisco_nxos)
	devices = (cisco_rtr1, cisco_rtr2)

	
	napalm_conns = []

	for a_device in devices:
		print("\n)")
		device_type = a_device.pop('device_type')
		driver = get_network_driver(device_type)
		device = driver(**a_device)
		napalm_conns.append(device)
		print(" ********************  DEVICE START  **********************")
		print("\n {} device created!".format(a_device['hostname']))
		device.open()
		print("\n Device connection opened of type {}!".format(device_type))
		lldp = device.get_lldp_neighbors()
		# model = facts['model']
		print("\n)")
		pprint(lldp)
		neighbors_list = []
		for key in lldp.keys():
			neighbor_list = neighbor_list.append(lldp[key][0]['hostname'])
			print("\n)")
		print(" ---------------------  DEVICE END  -----------------------")
		print("\n\n")
		print("")
	print(neighbor_list)
	print("The neighbors are:  {}".format(neighbor_list))

if __name__ == "__main__":
	main()


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

4. Using NAPALM retrieve get_interfaces from Arista switch2 (pynet_sw2). 
Find all of the interfaces that are in an UP-UP state (is_enabled=True, 
and is_up=True). Print all of these UP-UP interfaces to standard output.

output
{'Ethernet1': {'description': '',
               'is_enabled': True,
               'is_up': True,
               'last_flapped': 1538591527.2426357,
               'mac_address': '52:54:AB:02:A1:11',
               'speed': 0},
 'Ethernet2': {'description': '',
               'is_enabled': True,
               'is_up': True,
               'last_flapped': 1538591527.2428465,
               'mac_address': '52:54:AB:02:A1:12',
               'speed': 0},
 'Ethernet3': {'description': '',
               'is_enabled': True,
               'is_up': True,
               'last_flapped': 1538591527.2430475,
               'mac_address': '52:54:AB:02:A1:13',
               'speed': 0},

"""

def main():
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	password = getpass()
	devices = ()

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
	devices = (arista_sw2,) 
	print(devices)
	## Note that we need to change the logic below because when only one item in the tuple
	## the type(a_device) is no longer a dictionary, it is a 

	napalm_conns = []
	# pprint(devices)
	# print(type(devices))
	# print(len(devices))

	print("\n")
	print("\n")
	for a_device in devices:
		device_type = a_device.pop('device_type')
		driver = get_network_driver(device_type)
		device = driver(**a_device)
		napalm_conns.append(device)
		print(" ********************  DEVICE START  **********************")
		print("\nDevice created! Host: {}".format(a_device['hostname']))
		device.open()
		print("\nDevice connection opened! Type: {}".format(device_type))
		intfs = device.get_interfaces()
		pprint(intfs)
		for int, int_dict in intfs:
			print(int)
			print(int_dict)
			print("---------")
			print("\n")

		# is_up = bgp['global']['peers'][bgp_neighbor]['is_up']
		# print("\nBGP peer, {}, is_up status is {}".format(bgp_neighbor, is_up))
		print("\n")

		print(" ---------------------  DEVICE END  -----------------------")
		print("\n")



"""
device_type = devices.pop('device_type')
	driver = get_network_driver(device_type)
	device = driver(**devices)
	napalm_conns.append(device)
	print(" ********************  DEVICE START  **********************")
	print("\nDevice created! Host: {}".format(devices['hostname']))
	device.open()
	print("\nDevice connection opened! Type: {}".format(device_type))
	bgp = device.get_bgp_neighbors()
	pprint(bgp)

	is_up = bgp['global']['peers'][bgp_neighbor]['is_up']
	print("\nBGP peer, {}, is_up status is {}".format(bgp_neighbor, is_up))
	print("\n")

	print(" ---------------------  DEVICE END  -----------------------")
	print("\n")
	# print("\nThe bgp neighbors are:  {}".format(neighbor_list))
	# print("\nThe ports are:  {}".format(port_list))
"""



if __name__ == "__main__":
	main()

"""


"""



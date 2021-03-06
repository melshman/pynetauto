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

3. Using NAPALM retrieve 'get_bgp_neighbors' from pynet-rtr1. 
Parse the returned data structure to and verify that the BGP peer 
to 10.220.88.38 is in the established state ('is_up' field in the 
NAPALM returned data structure).

{'global': {'peers': {'10.220.88.38': {'address_family': {'ipv4': {'accepted_prefixes': 0,
                                                                   'received_prefixes': 0,
                                                                   'sent_prefixes': 0}},
                                       'description': '',
                                       'is_enabled': True,
                                       'is_up': True,
                                       'local_as': 42,
                                       'remote_as': 44,
                                       'remote_id': '10.220.88.38',
                                       'uptime': 1641600}},
            'router_id': '10.220.88.20'}}
BGP peer, 10.220.88.38, is_up status is True

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
	devices = (cisco_rtr1,) 
	print(devices)
	## Note that we need to change the logic below because when only one item in the tuple
	## the type(a_device) is no longer a dictionary, it is a 

	napalm_conns = []
	bgp_neighbor = '10.220.88.38'
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
		bgp = device.get_bgp_neighbors()
		pprint(bgp)

		is_up = bgp['global']['peers'][bgp_neighbor]['is_up']
		print("\nBGP peer, {}, is_up status is {}".format(bgp_neighbor, is_up))
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



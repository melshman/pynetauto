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

5. Using NAPALM and the one of the Cisco routers perform the following config operations:
a. Stage a change adding a /32 static route (merge operation). Use something in 1.1.X.X/32.
b. Perform a compare_config operation to see your staged change.
c. Discard your change.
d. Verify compare_config shows no pending changes (after your discard operation).
e. Re-stage your change adding a /32 static route (merge operation).
f. Commit your change.

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
		# merge_cantidate exist????
		print("\nLoading configuration merge file!")
		# device.load_merge_candidate(config = hostname rtr1)
		device.load_merge_candidate(filename = 'static_route.cfg')

		diff = device.compare_config()
		print("The difference between the current and staged configuration: \n{}".format(diff))
		
		choice = input("\nWould you like to commit these changes? [y/n]:  ")
		if choice =='y':
			print("Commiting... ")
			device.commit_config()
		else:
			print("Discarding... ")
			device.discard_config()

		print("Confirming that no pending changes remain")
		diff = device.compare_config()
		print(diff)
		# if diff == ""
		# 	print("\nNo remaining staged changes")
		# else:
		# 	print("\nStaged changes still remain!")
		print(" ---------------------  DEVICE END  -----------------------")




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



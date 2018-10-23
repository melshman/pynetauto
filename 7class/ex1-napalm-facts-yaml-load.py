#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from napalm import get_network_driver

# from my_devices import devices
import yaml

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint

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


	# cisco_rtr1 = {
	# 	'hostname' : '184.105.247.70',
	# 	'device_type' : 'ios',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {}
	# }
	# cisco_rtr2 = {
	# 	'hostname' : '184.105.247.71',
	# 	'device_type' : 'ios',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {}
	# }
	# arista_sw1 = {
	# 	'hostname' : '184.105.247.72',
	# 	'device_type' : 'eos',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {}
	# }
	# arista_sw2 = {
	# 	'hostname' : '184.105.247.73',
	# 	'device_type' : 'eos',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {}
	# }

	# jnpr_srx1 = {
	# 	'hostname' : '184.105.247.76',
	# 	'device_type' : 'junos',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {}
	# }
	# cisco_nxos = {
	# 	'hostname' : 'nxos1.twb-tech.com',
	# 	'device_type' : 'nxos',
	# 	'password' : password,
	# 	'username' : 'pyclass',
	# 	'optional_args' : {'port' : '8443',
	# 						'nxos_protocol' : 'https'
	# 	}
	# }



	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	password = getpass()
	yaml_file = 'my_devices.yaml'
	# yaml_file = 'kb.yaml'
	napalm_conns = []

	with open(yaml_file) as f:
		devices = yaml.load(f)
		pprint(devices)
		print("\n\n")
	# 	print("\n")
	# 	for device in devices:
	# 		print(" ********************  DEVICE START  **********************")
	# 		print(device)
	# 		for key in device.keys():
	# 			print("\n")
	# 			pprint(key)
	# 			print("\n")
	# 			pprint(device[key]['device_type'])
	# 		print(" ---------------------  DEVICE END  -----------------------")
	# 		print("")
	# 		print("")
	# 	pprint(devices[item_num]['cisco_rtr1']['device_type'])


	# for a_device in devices:
	# 	for key in a_device.keys():
	# 		device_type = a_device[key].pop('device_type')
	# 		# device_type = a_device.pop('device_type')
	# 		driver = get_network_driver(device_type)
	# 		device = driver(**a_device[key])
	# 		napalm_conns.append(device)
	# 		print("\n {} device created!".format(a_device[key]['hostname']))
	# 		device.open()
	# 		print("\n Device connection opened of type {}!".format(device_type))
	# 		print("\n")
	# 		facts = device.get_facts()
	# 		model = facts['model']
	# 		pprint(model)
	# 		print("\n\n")

	for a_device in devices:
		print(a_device)
		for device_name, device_dict in a_device.items():
			print("***************** START:  {}  *******************************".format(device_name))
			print("\n")
			print(device_dict)
			device_type = device_dict.pop('device_type')
			print("The Device Type is:  {}".format(device_type))
			driver = get_network_driver(device_type)
			# Set the password
			device_dict['password'] = password
			device = driver(**device_dict) 
			napalm_conns.append(device)
			print("\nnapalm_comms is equal to: {} ".format(napalm_conns))
			print("\n{} device created!".format(device_dict['hostname']))
			device.open()
			print("\nDevice connection opened of type {}!".format(device_type))
			print("\n")
			facts = device.get_facts()
			print("the facts are: {} ".format(facts))
			device_model = facts['model']
			print("The Model of this device is: {}  ".format(device_model))
			print("\n")
			print("***************** END:  {}  *******************************".format(device_name))
			print("\n\n")

if __name__ == "__main__":
	main()


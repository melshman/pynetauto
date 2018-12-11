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


5. Create NAPALM a script that connects to srx1 and retrieves its LLDP information 
(get_lldp_neighbors() method).

From this returned data structure retrieve the local interface name, the remote 
switch name that this srx1 is connected to, and the remote port name.

Email this local interface, remote switch name, and remote port name to yourself 
using the send_mail function from earlier in the course.

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
	devices = (jnpr_srx1,)

	
	napalm_conns = []
	neighbor_list = []
	port_list = []
	for a_device in devices:
		# print("\n")
		# pprint(a_device)
		print("\n")
		device_type = a_device.pop('device_type')
		driver = get_network_driver(device_type)
		device = driver(**a_device)
		napalm_conns.append(device)
		print(" ********************  DEVICE START  **********************")
		print("\nDevice created! Host: {}".format(a_device['hostname']))
		device.open()
		print("\nDevice connection opened! Type: {}".format(device_type))
		lldp = device.get_lldp_neighbors()
		print("\n{}\n".format(lldp))

		for key in lldp.keys():
			local_int = key
			remote_device = lldp[key][0]['hostname']
			remote_port = lldp[key][0]['port']
			print("local interface {} has a neighbor {} connected on remote port {}".format(local_int, remote_device, remote_port))

	# 	for key in lldp.keys():
	# 		neighbor_list.append(lldp[key][0]['hostname'])
	# 		port_list.append(lldp[key][0]['port'])
	# 	print(" ---------------------  DEVICE END  -----------------------")
	# 	print("\n")
	# print("\nThe neighbors are:  {}".format(neighbor_list))
	# print("\nThe ports are:  {}".format(port_list))

if __name__ == "__main__":
	main()


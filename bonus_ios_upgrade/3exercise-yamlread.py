#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from getpass import getpass
from netmiko import ConnectHandler, file_transfer
from pprint import pprint
import yaml


"""

3. Update exercise2 such that you store the definition for the four 
Arista devices in an external YAML file that you read in and parse 
upon script execution.

You should use the device definition in this external YAML file to 
make the Netmiko connections.

In other words, make your key-value pairs in your YAML dictionary match 
the key-value pairs that you require for Netmiko.

Don't include the password in your YAML file. Add the password file 
using getpass() to the device dictionary inside of your Python program.


"""

def main():
	password = getpass()

	net_devices = []

	# USE FOR PYNET AWS LAB
	with open("net_devices.yaml", 'r') as f:
		try:
			net_devices = yaml.load(f)
		except yaml.YAMLError as exc:
			print(exc)

	## USE FOR LOCAL LAB USE
	# with open("local_net_devices.yaml", 'r') as f:
	# 	try:
	# 		net_devices = yaml.load(f)
	# 	except yaml.YAMLError as exc:
	# 		print(exc)


	## THSOOT
	# pprint(net_devices)
	# pprint(type(net_devices))


	source_file = 'my_file3.txt'
	dest_file = 'transfered_file.txt'
	direction = 'put'

	for net_device in net_devices:

		net_device['password'] = password
		file_system = net_device.pop('file_system')  

	    #TSHOOT
	    # pprint(net_device)
	    # pprint(type(net_device))
	    # pprint(net_device['password'])


	    # Create the Netmiko SSH connection
		ssh_conn = ConnectHandler(**net_device)
		transfer_dict = file_transfer(ssh_conn,
	                                  source_file=source_file, 
	                                  dest_file=dest_file,
	                                  file_system=file_system, 
	                                  direction=direction,
	                                  overwrite_file=True)
		print("Transfer_dict for {}:  {}".format(net_device['host'],transfer_dict))

		if transfer_dict['file_verified']==True:
			print("The MDF has been verfied.  The file transfer was successful!")
		else:
			print("The MDF could not be verfied.  The file transfer was NOT successful!  Please try again")

		pause = input("Hit enter to continue: ")

if __name__ == '__main__':
	main()


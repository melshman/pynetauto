#!/usr/bin/env python
from __future__ import print_function, unicode_literals

from getpass import getpass
from netmiko import ConnectHandler, file_transfer
from pprint import pprint

"""

2. Create a file named 'my_file.txt' with some random content in it.

Use Netmiko's secure copy to transfer this file to the Arista1, Arista2, Arista3, and Arista4 switches.

Note, you will need to use PIP to upgrade Netmiko in the lab environment to Netmiko 2.1.1 to complete this exercise:
$ pip install netmiko==2.1.1

At the end of the transfer make sure the file exists and the MD5 passed. Netmiko should report this back to you as part of its file_transfer function.

Optional Bonus: Use threads so this transfer happens on all four switches concurrently.


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

	Arista1 = { 
	    'device_type': 'arista_eos',
	    'host': '184.105.247.72',
	    'username': 'pyclass',
	    'password': password,
	    'file_system': '/mnt/flash'
	    }

	Arista2 = { 
	    'device_type': 'arista_eos',
	    'host': '184.105.247.73',
	    'username': 'pyclass',
	    'password': password,
	    'file_system': '/mnt/flash'
	    }

	Arista3 = { 
	    'device_type': 'arista_eos',
	    'host': '184.105.247.74',
	    'username': 'pyclass',
	    'password': password,
	    'file_system': '/mnt/flash'
	    }

	Arista4 = { 
	    'device_type': 'arista_eos',
	    'host': '184.105.247.75',
	    'username': 'pyclass',
	    'password': password,
	    'file_system': '/mnt/flash'
	    }

	source_file = 'my_file1.txt'
	dest_file = 'transfered_file.txt'
	direction = 'put'

	# can add additional devices ; need ',' when tuple is only one value
	# use this for statement for local lab switches
	for net_device in (VTswitch, switch07):
		
	# use for pynet AWS lab environment	
	# for net_device in (Arista1, Arista2, Arista3, Arista4):

	    # have to pop so that the remaining dict will satisfy Netmiko ConnectHandler
	    file_system = net_device.pop('file_system')  

	    # Create the Netmiko SSH connection
	    ssh_conn = ConnectHandler(**net_device)
	    transfer_dict = file_transfer(ssh_conn,
	                                  source_file=source_file, 
	                                  dest_file=dest_file,
	                                  file_system=file_system, 
	                                  direction=direction,
	                                  overwrite_file=True)
	    pprint(transfer_dict)
	    pause = input("Hit enter to continue: ")

	    if transfer_dict['file_verified']==True:
	    	print("The MD5 has been verfied.  The file transfer was successful!")
	    else:
	    	print("The MD5 could not be verfied.  The file transfer was NOT successful!  Please try again")


if __name__ == '__main__':
	main()


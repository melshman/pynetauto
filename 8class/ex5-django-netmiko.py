#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from __future__ import print_function, unicode_literals
import django
jango.setup()
from net_system.models import NetworkDevice, Credentials

'''

5. Use Netmiko to connect to each of the devices in the database. 
Execute 'show version' on each device. Calculate the amount of time 
required to do this. 

'''

def main():
	net_devices = NetworkDevice.objects.all()
	start_time = datetime.now()
	print("\n{}".format(start_time))
	print("\n")
	for a_device in net_devices:
		print(a_device)
		net_connect = ConnectHandler(**a_device)
		config_commands = ['show version']
		output = net_connect.send_config_set(config_commands)
		print("\n\n****************************\n")
		print("{}".format(output))
		print("\n\n----------------------------\n")
	end_time = datetim.now()
	elapsed = end_time - start_time
	print("\n{}".format(elapsed)


if __name__ == "__main__":
	main()


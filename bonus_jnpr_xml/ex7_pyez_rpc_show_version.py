#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

from jnpr.junos import Device
# from jnpr.junos.op.ethport import EthPortTable
# from jnpr.junos.op.arp import ArpTable
# from jnpr.junos.op.routes import RouteTable
# from jnpr.junos.op.phyport import PhyPortTable
# from jnpr.junos.op.phyport import PhyPortStatsTable
from jnpr.junos.utils.config import Config

'''

7. Use Juniper's PyEZ and direct RPC to retrieve the XML for 
'show version' from the Juniper SRX.

Print out this returned XML as a string using 'etree.tostring()'. 
Parse the returned XML to retrieve the model from the device. 
Print this model number to the screen.

get-software-information

'''


def main():
	pwd = getpass()

	srx = {
		"hostname" : "srx1.twb-tech.com",
		"host" : "184.105.247.76",
		"user" : "pyclass",
		"password" : pwd
	}

	srx_device = Device(**srx)
	srx_device.open()

	print("\nThe current timeout is {} seconds.".format(srx_device.timeout))
	srx_device.timeout = 120
	print("\nThe updated timeout is {} seconds.".format(srx_device.timeout))

	print("\n")
	show_version = srx_device.rpc.get_software_information
	pprint(show_version)
	print("\n")
	print(etree.tostring(show_version, encoding='unicode', pretty_print=True))


if __name__ == "__main__":
	main()



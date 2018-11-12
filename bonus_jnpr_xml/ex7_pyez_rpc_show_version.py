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
	pprint(srx_device.facts)
	print("\n")

	cfg = Config(srx_device)
	cfg.load("set system host-name testsrx", format="set", merge=True)
	print(cfg.diff())
	cfg.rollback(0)
	print("\nROLLED BACK... DENIED")

	cfg.load("set system host-name testsrx", format="set", merge=True)
	print(cfg.diff())
	cfg.commit()
	print("\ntestsrx COMMITED")

	cfg.load("set system host-name pynet-jnpr-srx1", format="set", merge=True)
	print(cfg.diff())
	cfg.commit()
	print("\nBACK TO NORM with pynet-jnpr-srx1")






if __name__ == "__main__":
	main()



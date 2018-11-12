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

6. Use the PyEZ load() method to set the hostname of the SRX using set, 
conf (curly brace), and XML formats.

After each load(), display the differences between the running config 
and the candidate config. Additionally, perform at least one commit and 
one rollback(0) in this program.

The committed hostname at the end of the program should be:  pynet-jnpr-srx1

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



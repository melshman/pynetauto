#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

from jnpr.junos import Device
# from jnpr.junos.op.ethport import EthPortTable
# from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable
# from jnpr.junos.op.phyport import PhyPortTable
# from jnpr.junos.op.phyport import PhyPortStatsTable
# from jnpr.junos.utils.config import Config

'''

5. Display the SRX's routing table. You will probably want to use 
RouteTable for this (from jnpr.junos.op.routes import RouteTable).

The output should look similiar to the following:

Juniper SRX Routing Table: 
0.0.0.0/0
  nexthop 10.220.88.1
  age 14582542
  via vlan.0
  protocol Static

10.220.88.0/24
  nexthop None
  age 14583120
  via vlan.0
  protocol Direct

10.220.88.39/32
  nexthop None
  age 14583289
  via vlan.0
  protocol Local


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

	routes = RouteTable(srx_device)
	routes.get()

	routes_dict = {}

	for item in routes.items():
		route = item[0]
		nexthop = item[1][3]
		age = item[1][2]
		via = item[1][1]
		protocol = item[1][0]
	
	routes_dict.update({
		route: {
			"nexthop" : nexthop,
			"age" : age,
			"via" : via,
			"protocol" : protocol
			}
		})

			
	# 	routes_dict.update({
	# 		intf:{
	# 			"operational state" : op_state,
	# 			"packets in" : rx_packets,
	# 			"packets out" : rx_packets			
	# 			}
	# 		})
	
	# print("\n")
	# pprint(routes_dict)


	print("\nJust the intfs ma'am")
	print("*******************")
	pprint(routes)
	print("*******************\n")
	

if __name__ == "__main__":
	main()



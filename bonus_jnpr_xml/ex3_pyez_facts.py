#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

from jnpr.junos import Device
# from jnpr.junos.op.ethport import EthPortTable
# from jnpr.junos.op.arp import ArpTable
# from jnpr.junos.op.phyport import PhyPortTable
# from jnpr.junos.op.phyport import PhyPortStatsTable
# from jnpr.junos.utils.config import Config

'''

3. Use Juniper's PyEZ library to make a connection to the Juniper SRX 
and to print out the device's facts.


'''


def main():
pwd = getpass()

srx = {
	"hostname" : "srx1.twb-tech.com",
	"host" : "184.105.247.76",
	"username" : "pyclass",
	"password" : "pwd"
}

srx_device = Device(**srx)
srx_device.open()

	print("The current timeout is {} seconds.".format(srx_device.timeout))
	srx_device.timeout = 120
	print("The updated timeout is {} seconds.".format(srx_device.timeout))

	facts = srx_device.get_facts()

	# print(etree.tostring(lldp, encoding='unicode', pretty_print=True).decode().rstrip())
	# print(etree.tostring(lldp, encoding='unicode', pretty_print=True).decode())
	print("\n")
	print(etree.tostring(arp, encoding='unicode', pretty_print=True))
	print("\n")

	# pprint(arp.xpath("/arp-table-information/arp-table-entry/mac-address"))
	arp_dict = {}
	for entry in arp.xpath("/arp-table-information/arp-table-entry"):
		for val in entry:
			# print("{}:  {}".format(val.tag, val.text))
			if val.tag == 'hostname':
				host = val.text
			elif val.tag == 'interface-name':
				intf = val.text
			elif val.tag == 'mac-address':
				mac_addr = val.text
		arp_dict.update({
			host:{
				'intf': intf,
				'mac_addr': mac_addr,
			}
		})
	pprint(arp_dict)
	print("\n")
	# pprint(lldp.getchildren())





	# arp_dict = {
	# 	local_int: {
	# 		'remote_sys_name': remote_sys,
	# 		'remote_port': remote_port,
	# 	}
	# }

	# pprint(arp_dict)


# print(lldp.getchildren())
# print(entry1[0].text)
# print(entry1[1].text)
# print(lldp[0][0].tag)     ## 'lldp-local-interface'
# print(lldp[0][0].text)   ## 'fe-0/0/7.0'


if __name__ == "__main__":
	main()


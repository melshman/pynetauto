#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

'''

2. Read in the file named 'show_arp.xml' (see GitHub repository link). 
This file is from 'show arp | display xml' on a Juniper SRX (modified somewhat).

Use etree.tostring() to print out the XML tree as a string.

Use XPath parsing to find all of the arp entries and to construct the following dictionary:

{
'10.220.88.1':
{
'intf': 'vlan.0',
'mac_addr': '00:62:ec:29:70:fe'
},
'10.220.88.20':
{
'intf': 'vlan.0',
'mac_addr': 'c8:9c:1d:ea:0e:b6'
}
}

Print this dictionary out to standard output.

<hostname>10.220.88.1</hostname>
<interface-name>vlan.0</interface-name>
<mac-address>00:62:ec:29:70:fe</mac-address>

intf
mac_addr


'''


def main():

	with open('show_arp.xml') as f:
		arp = etree.fromstring(f.read())

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


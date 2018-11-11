#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

# from jnpr.junos import Device
# from jnpr.junos.op.ethport import EthPortTable
# from jnpr.junos.op.arp import ArpTable
# from jnpr.junos.op.phyport import PhyPortTable
# from jnpr.junos.op.phyport import PhyPortStatsTable
# from jnpr.junos.utils.config import Config



'''

1. Read in the file named 'show_lldp.xml' (see GitHub repository link). This file is from 'show lldp 
neighbors | display xml' on a Juniper SRX (modified somewhat).

Use etree.tostring() to print out the XML tree as a string.

Use getchildren() or list indices to find the one child element of the root element. 
Print out this element's tag name.

Using either a for-loop or getchildren(), find the text values associated with the following tags: 
'lldp-local-interface', 'lldp-remote-system-name', 'lldp-remote-port-description'. Save these three 
items to a data structure with the following format:
{ local_intf:
  {
    'remote_port': value,
    'remote_sys_name': value,
  }
}
Print this data structure out to the screen. Your printed data structure should match the following:
{'fe-0/0/7.0': 
    {
        'remote_port': '24', 
        'remote_sys_name': 'twb-sf-hpsw1'
    }
}

'''

def main():

	with open('show_lldp.xml') as f:
		lldp = etree.fromstring(f.read())

	# print(etree.tostring(lldp, encoding='unicode', pretty_print=True).decode().rstrip())
	# print(etree.tostring(lldp, encoding='unicode', pretty_print=True).decode())
	print(etree.tostring(lldp, encoding='unicode', pretty_print=True))

	# pprint(lldp.getchildren())
	lldp_child = lldp.getchildren()[0]
	print(lldp_child.tag)


	for child in lldp_child:
		if child.tag == 'lldp-local-interface':
			local_int = child.text
		elif child.tag == 'lldp-remote-system-name':
			remote_sys = child.text
		elif child.tag == 'lldp-remote-port-description':
			remote_port = child.text

	lldp_dict = {
		local_int: {
			'remote_sys_name': remote_sys,
			'remote_port': remote_port,
		}
	}

	pprint(lldp_dict)


# print(lldp.getchildren())
# print(entry1[0].text)
# print(entry1[1].text)
# print(lldp[0][0].tag)     ## 'lldp-local-interface'
# print(lldp[0][0].text)   ## 'fe-0/0/7.0'


if __name__ == "__main__":
	main()


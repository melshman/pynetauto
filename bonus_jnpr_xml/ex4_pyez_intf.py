#!/usr/bin/env python

from getpass import getpass
from pprint import pprint

from lxml import etree
# import xmltodict

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from jnpr.junos.op.arp import ArpTable
# from jnpr.junos.op.phyport import PhyPortTable
# from jnpr.junos.op.phyport import PhyPortStatsTable
# from jnpr.junos.utils.config import Config

'''

4. For each of the SRX's interfaces, display: the operational state, 
packets-in, and packets-out. You will probably want to use EthPortTable 
for this.


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

	intfs = EthPortTable(srx_device)
	intfs.get()

	intfs_dict = {}

	for item in intfs.items():
		intf = item[0]
		op_state = item[1][0][1]
		rx_packets = item[1][7][1]
		tx_packets = item[1][9][1]
			
		# intfs_dict.update({
		# 	"interface" : intf,
		# 	"operational state" : op_state,
		# 	"packets in" : rx_packets,
		# 	"packets out" : rx_packets
		# 	})

		intfs_dict.update({
			intf:{
				"operational state" : op_state,
				"packets in" : rx_packets,
				"packets out" : rx_packets			
				}
			})
	print("\n")
	pprint(intfs_dict)


	print("\nJust the intfs ma'am")
	print("*******************")
	pprint(intfs)
	print("*******************\n")

	pprint(intfs_dict['fe-0/0/7'])
	print("\n")
	pprint(intfs_dict['fe-0/0/7']['packets in'])
	print("\n")
	
	# uptime = facts['RE0']['up_time']
	# reboot_reason = facts['re_info']['default']['0']['last_reboot_reason']
	
	# print("The last time this router was reboot, was {} ago and the cause was {}.\n".format(uptime, reboot_reason))



if __name__ == "__main__":
	main()



'''
looking around in facts dict

In [25]: facts['fqdn']
Out[25]: 'pynet-jnpr-srx1'

In [26]: facts['re_info']
Out[26]:
{'default': {'0': {'mastership_state': 'master',
   'status': 'OK',
   'model': 'RE-SRX100H2',
   'last_reboot_reason': '0x1:power cycle/failure'},
  'default': {'mastership_state': 'master',
   'status': 'OK',
   'model': 'RE-SRX100H2',
   'last_reboot_reason': '0x1:power cycle/failure'}}}

In [27]: facts['re_info']['default']
Out[27]:
{'0': {'mastership_state': 'master',
  'status': 'OK',
  'model': 'RE-SRX100H2',
  'last_reboot_reason': '0x1:power cycle/failure'},
 'default': {'mastership_state': 'master',
  'status': 'OK',
  'model': 'RE-SRX100H2',
  'last_reboot_reason': '0x1:power cycle/failure'}}

In [28]: facts['re_info']['default']['0']
Out[28]:
{'mastership_state': 'master',
 'status': 'OK',
 'model': 'RE-SRX100H2',
 'last_reboot_reason': '0x1:power cycle/failure'}

In [29]: facts['re_info']['default']['0']['last_reboot_reason']
Out[29]: '0x1:power cycle/failure'


'''


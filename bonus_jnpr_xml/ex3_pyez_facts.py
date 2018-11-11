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
		"user" : "pyclass",
		"password" : pwd
	}

	srx_device = Device(**srx)
	srx_device = Device()
	srx_device.open()

	print("The current timeout is {} seconds.".format(srx_device.timeout))
	srx_device.timeout = 120
	print("The updated timeout is {} seconds.".format(srx_device.timeout))

	facts = srx_device.facts

	pprint(facts)
	
	uptime = facts['RE0']['up_time']
	reboot_reason = facts['re_info']['default']['0']['last_reboot_reason']
	
	pprint("The last time this router was reboot, was {} ago and the cause was {}".format(uptime, reboot_reason))



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


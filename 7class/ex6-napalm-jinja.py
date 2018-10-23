#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from napalm import get_network_driver
# from my_devices import devices
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

"""

6. [Optional] - Use Jinja2 templating to generate the DNS configurations 
for Cisco IOS, Arista EOS, and Cisco NX-OS.

Note, in the reference solutions, I implemented this in two different ways. 
Solution1 (named napalm_ex6.py) uses the integrated Jinja2 templating that NAPALM 
provides via the load_template() method. Solution2 (named napalm_ex6_alt.py) uses 
standard Jinja2 templating that we learned about previously. 

Your templates should look as follows:
-------
$ cat ios/dns.j2 
ip name-server 
ip name-server 
ip domain-lookup

$ cat eos/dns.j2 
ip name-server vrf default 
ip name-server vrf default 

$ cat nxos/dns.j2 
ip name-server   use-vrf management
-------

From these Jinja2 templates, generate three config files 
named 'dns.txt' (corresponding to each of the platforms):
$ tree
.
├── eos
│   ├── dns.j2
│   └── dns.txt
├── ios
│   ├── dns.j2
│   └── dns.txt
└── nxos
    ├── dns.j2
    └── dns.txt

For dns1 use '1.1.1.1'; for dns2 use '8.8.8.8'.

After you configurations have been generated from the Jinja2 templates, 
then use a NAPALM merge operation to push and commit the new DNS configurations. 
You should push the relevant configuration to the following 
devices 'pynet-rtr1' (Cisco IOS), 'pynet-sw1' (Arista EOS), 'nxos1' (Cisco NX-OS).

Finally, after the configuration changes have been pushed, use the NAPALM 
'ping' method to ping google.com and thus verify that the DNS is working properly.

napalm_object.ping(destination='google.com')

You should verify that at least one ping to google.com comes back successfully. 
Note, the NX-OS device will probably fail on the ping (including potentially 
generating a NotImplementedError exception that you should gracefully catch).

"""

def ping_google():
	"""Use NAPALM to ping google.com to validate DNS resolution."""
	print()
	print(">>>Test ping to google.com")
	try:
		ping_output = device.ping(destination='google.com')
	except NotImplementedError:
		print("Ping failed: ping() method not implemented")
		return
	if not ping_output == {}:
		probes_sent = int(ping_output['success']['probes_sent'])
		packet_loss = int(ping_output['success']['packet_loss'])
		successful_pings = probes_sent - packet_loss
		print("Probes sent: {}".format(probes_sent))
		print("Packet loss: {}".format(packet_loss))
		if successful_pings > 0:
			print("Pings Successful: {}".format(successful_pings))
			return

	print("Ping failed")




def main():
	requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
	password = getpass()

	cisco_rtr1 = {
		'hostname' : '184.105.247.70',
		'device_type' : 'ios',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	cisco_rtr2 = {
		'hostname' : '184.105.247.71',
		'device_type' : 'ios',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	arista_sw1 = {
		'hostname' : '184.105.247.72',
		'device_type' : 'eos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	arista_sw2 = {
		'hostname' : '184.105.247.73',
		'device_type' : 'eos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	jnpr_srx1 = {
		'hostname' : '184.105.247.76',
		'device_type' : 'junos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {}
	}
	cisco_nxos = {
		'hostname' : 'nxos1.twb-tech.com',
		'device_type' : 'nxos',
		'password' : password,
		'username' : 'pyclass',
		'optional_args' : {'port' : '8443',
							'nxos_protocol' : 'https'
		}
	}


	# devices = (cisco_rtr1, cisco_rtr2, arista_sw1, arista_sw2, jnpr_srx1, cisco_nxos)
	# devices = (cisco_rtr1, cisco_rtr2)
	devices = (cisco_rtr1, cisco_rtr2, arista_sw1, arista_sw2, cisco_nxos)

	napalm_conns = []

	template_vars = {
			'dns1': '1.1.1.1',
			'dns2': '8.8.8.8',
			}

	base_path = '/home/tarmstrong/projects/pynetauto/7class'


	for a_device in devices:
		# print("\n")
		# pprint(a_device)
		print("\n")
		device_type = a_device.pop('device_type')
		driver = get_network_driver(device_type)
		device = driver(**a_device)
		napalm_conns.append(device)
		print(" ********************  DEVICE START  **********************")
		print("\nDevice created! Host: {}".format(a_device['hostname']))
		device.open()
		print("\nDevice connection opened! Type: {}".format(device_type))
		
		device.load_template("dns", template_path=base_path, **template_vars)
        print(device.compare_config())
        device.commit_config()



if __name__ == "__main__":
	main()


#!/usr/bin/env python


"""
3. Expand upon exercise2 to generate the following:
--------
interface Loopback0
 ip address 172.31.255.1 255.255.255.255

router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
 network 172.31.255.28 0.0.0.0 area 1
--------

The Jinja2 template should be read from an external file named 'ospf_config_for.j2'.

The OSPF 'network' statements should be generated using a for-loop embedded in the Jinja2 template.

You should have a Python data structure named 'ospf_networks' that you iterate over 
(in your Jinja2 for-loop). At the highest-level this data structure should be either a list 
or a dictionary.

The following items should all be variables in the template:
process_id
network*
wildcard*
area*
loopback0_addr
loopback0_maks

* Contained inside of the ospf_networks variable

Additionally, the interface Loopback0 and its ip address config should only be generated 
if the loopback0_addr variable is defined (i.e. use an if-condition here).
"""


from __future__ import unicode_literals, print_function
# from jinja2 import FileSystemLoader, StrictUndefined
# from jinja2.environment import Environment
import jinja2
from getpass import getpass


ospf_networks = [
    {
	    'net_addr' : '10.220.88.0',
	    'net_mask' : '0.0.0.255',
	    'net_area' : '0'
	},
	{
	    'net_addr' : '172.31.255.28',
	    'net_mask' : '0.0.0.0',
	    'net_area' : '1'
	}
]

# ospf_vars = {
#     'process_id': 40,
#     'ospf_networks': ospf_networks,
#     'loopback0_addr': '172.31.255.1',
#     'loopback0_mask': '255.255.255.255'
# }

loopback_vars = {
    'loopback0_addr': '172.31.255.1',
    'loopback0_mask': '255.255.255.255'
}

ospf_vars = {
    'process_id': 40,
    'ospf_networks': ospf_networks,
    'loopback_vars': loopback_vars
}

#### using external file - 'ospf_config.j2'
# ospf_config = '''
# router ospf {{ process_id }}
#  network {{network}} {{wildcard_mask}} area {{area}}
# '''



def main():
    with open("ospf_config_for.j2") as f:
    	ospf_config = f.read()
    
    template = jinja2.Template(ospf_config)
    output = template.render(**ospf_vars)
    print(output)

if __name__ == '__main__':
    main()

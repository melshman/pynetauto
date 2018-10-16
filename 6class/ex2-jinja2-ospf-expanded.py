#!/usr/bin/env python


"""
2. Expand upon exercise1 to generate the following:
--------
interface Loopback0
 ip address 172.31.255.1 255.255.255.255

router ospf 40
 network 10.220.88.0 0.0.0.255 area 0
--------

The Jinja2 template should be read from an external file named 'ospf_config.j2'.

The following items should all be variables in the template: process_id, network, 
wildcard, area, loopback0_addr, loopback0_mask.

Additionally, the 'interface Loopback0' and its ip address configuration should only 
be generated if the loopback0_addr variable is defined (i.e. use an if-condition here).

"""


from __future__ import unicode_literals, print_function
# from jinja2 import FileSystemLoader, StrictUndefined
# from jinja2.environment import Environment
import jinja2
from getpass import getpass


ospf_vars = {
	'process_id' : '40',
	'network' : '10.220.88.0',
	'wildcard_mask' : '0.0.0.255',
	'area' : '0'
}

loopback_vars = {
	'loopback0_addr' : '172.31.255.1',
	'loopback0_mask' : '255.255.255.255'
}

#### using external file - 'ospf_config.j2'
# ospf_config = '''
# router ospf {{ process_id }}
#  network {{network}} {{wildcard_mask}} area {{area}}
# '''



def main():
    with open("ospf_config.j2") as f:
    	ospf_config = f.read()
    
    template = jinja2.Template(ospf_config)
    output = template.render(**ospf_vars, **loopback_vars)
    print(output)

if __name__ == '__main__':
    main()

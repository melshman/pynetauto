#!/usr/bin/env python


"""
6. Use the pynxos library and NX-API to retrieve the output of 
'show ip route vrf management' from the nxos1 switch. 
Parse the returned data structure and from this, retrieve the 
next hop for the default route. Print this to standard output.
"""


from __future__ import unicode_literals, print_function
# from jinja2 import FileSystemLoader, StrictUndefined
# from jinja2.environment import Environment
from pynxos.device import Device
from getpass import getpass
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def main():
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    for host in ['nxos1.twb-tech.com', 'nxos2.twb-tech.com']:
	    device = Device(host=host,
	    	username='pyclass',
	    	password=getpass(),
	    	transport='https',
	    	port=8443)
	    print(device.show('show ip route vrf management'))

if __name__ == '__main__':
    main()

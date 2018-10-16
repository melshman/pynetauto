#!/usr/bin/env python


"""
5. Use the pynxos library to create an NX-API connection to both 
nxos1.twb-tech.com and to nxos2.twb-tech.com.

Use the pynxos 'show' method to retrieve 'show hostname' from 
each of the devices. Print this show hostname output to standard output.
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
	    print(device.show('show hostname'))

if __name__ == '__main__':
    main()

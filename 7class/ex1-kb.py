#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint

from napalm import get_network_driver

# from my_devices import devices
import yaml

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pprint import pprint


def main():

    password = getpass()
    yaml_file = 'kb.yaml'

    napalm_conns = []

    with open(yaml_file) as f:
        devices = yaml.load(f)
        # pprint(devices)

    for a_device in devices:
        # print(a_device)
        for device_name, device_dict in a_device.items():
            print(device_name)
            # pprint(device_dict)
            device_type = device_dict.pop('device_type')
            print(device_type)
            driver = get_network_driver(device_type)
	    # Set the password
            device_dict['password'] = password
            device = driver(**device_dict) 
            napalm_conns.append(device)
            print("\n {} device created!".format(device_dict['hostname']))
            device.open()
            print("\n Device connection opened of type {}!".format(device_type))
            print("\n")
            facts = device.get_facts()
            model = facts['model']
            print(model)
            print("\n\n")


if __name__ == "__main__":
    main()

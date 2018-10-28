#!/usr/bin/env python
"""
Using Netmiko enter into configuration mode on a network device.

Verify that you are currently in configuration mode.
"""
from __future__ import print_function, unicode_literals
from getpass import getpass
from netmiko import ConnectHandler
from test_devices import pynet1, pynet2, juniper_srx


def main():
    """
    Using Netmiko enter into configuration mode on a network device.

    Verify that you are currently in configuration mode.
    """
    password = getpass()

    for a_dict in (pynet1, pynet2, juniper_srx):
        a_dict['password'] = password
    net_connect2 = ConnectHandler(**pynet2)
    net_connect2.config_mode()
    print("\n>>>>")
    print("Checking pynet-rtr2 is in configuration mode.")
    print("Config mode check: {}".format(net_connect2.check_config_mode()))
    print("Current prompt: {}".format(net_connect2.find_prompt()))
    print(">>>>\n")


if __name__ == "__main__":
    main()

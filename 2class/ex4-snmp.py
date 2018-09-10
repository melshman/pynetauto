#!/usr/bin/env python
"""
Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
prints out both the MIB2 sysName and sysDescr.
"""

from __future__ import print_function, unicode_literals
import getpass
import pysnmp
import snmp_helper
from printout import printout

SYS_DESCR = '1.3.6.1.2.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'
OIDs = [SYS_DESCR, SYS_NAME]

def main():
    """
    Create a script that connects to both routers (pynet-rtr1 and pynet-rtr2) and
    prints out both the MIB2 sysName and sysDescr.
    """
    try:
        ip_addr1 = raw_input("pynet-rtr1 IP address: ")
        ip_addr2 = raw_input("pynet-rtr2 IP address: ")
    except NameError:
        ip_addr1 = input("pynet-rtr1 IP address: ")
        ip_addr2 = input("pynet-rtr2 IP address: ")
    community_string = getpass.getpass(prompt="Community string: ")

    pynet_rtr1 = (ip_addr1, community_string, 161)
    pynet_rtr2 = (ip_addr2, community_string, 161)
    routers = [pynet_rtr1, pynet_rtr2]
    # routers = [pynet_rtr1]

    for a_device in routers:
        print("\n*********************")
        for the_oid in OIDs:
            snmp_data = snmp_helper.snmp_get_oid(a_device, oid=the_oid)
            output = snmp_helper.snmp_extract(snmp_data)

            printout(output)
    print()


if __name__ == "__main__":
    main()
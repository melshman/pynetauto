#!/usr/bin/env python
"""
Use Arista's eAPI to obtain 'show interfaces' from the switch.  Parse the 'show
interfaces' output to obtain the 'inOctets' and 'outOctets' fields for each of
the interfaces on the switch.  Accomplish this using Arista's pyeapi library.
"""
from __future__ import print_function, unicode_literals
import pyeapi
import six


def pyeapi_result(output):
    """Return the 'result' value from the pyeapi output."""
    return output[0]['result']


def main():
    """Use Arista's eAPI to obtain 'show interfaces' from the switch."""
    eapi_conn = pyeapi.connect_to("pynet-sw2")

    interfaces = eapi_conn.enable("show interfaces")
    print(interfaces)
    print("\n")
    interfaces = pyeapi_result(interfaces)
    print(interfaces)
    print("\n")
    # Strip off unneeded dictionary
    interfaces = interfaces['interfaces']
    print(interfaces)
    print("\n")
    # inOctets/outOctets are fields inside 'interfaceCounters' dict
    data_stats = {}
    for interface, int_values in interfaces.items():
        int_counters = int_values.get('interfaceCounters', {})
        data_stats[interface] = (int_counters.get('inOctets'), int_counters.get('outOctets'))
    
    # Print output data
    print("\n")
    print(data_stats)
    print("\n")
    print("\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets"))
    for intf, octets in sorted(data_stats.items()):
        print("{:20} {:<20} {:<20}".format(intf, six.text_type(octets[0]),
                                           six.text_type(octets[1])))

    print()


if __name__ == '__main__':
    main()


# start by im:porting the library
import pyeapi
from pprint import pprint
import json
from getpass import getpass
import jinja2


def main():
    # create a node object by specifying the node to work with
    node = pyeapi.connect_to('pynet-sw3')

    # send one or more commands to the node
    r_ints = node.enable('show interfaces')
    pprint(r_ints)


# this interfaces var is currently not what I need
#interfaces = result[0]['result']['interfaces'].keys()

# TSHOOT INDIVIDUAL INT
    print("/n")
    ints = r_ints[0]['result']['interfaces']
    print("/n")
    pprint(ints)
    
    inOct = r_ints[0]['result']['interfaces']['Ethernet2']['interfaceCounters']['inOctets']
    outOct = r_ints[0]['result']['interfaces']['Ethernet2']['interfaceCounters']['outOctets']
    print("/n")
    print("Interface {}: inOctet = {} AND outOctets = {}".format('Ethernet2', inOct, outOct))

    for int, value in ints.items():
        if int == 'Vlan1':
            continue
        else:
            pprint("starting interface: {}".format(int))
            inOct  = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['inOctets']
            outOct = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['outOctets']
            print("Interface {}: inOctet = {} AND outOctets = {}".format(int, inOct, outOct))

# not working due to interfaces being a class... 
# and I can't figure out how to access the list contained within
#for int in interfaces:
#     inOct = result[0]['result']['interfaces'][{int}]['interfaceCounters']['inOctets']
#     outOct = result[0]['result']['interfaces'][{int}]['interfaceCounters']['outOctets']
#     print("Interface {}: inOctet = {} AND outOctets = {}".format(int, inOct, outOct))  


if __name__ == "__main__":
    main()

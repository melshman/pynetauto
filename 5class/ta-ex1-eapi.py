
# start by im:porting the library
import pyeapi
from pprint import pprint


def tshoot_ints(r_ints, ints):
# TSHOOT INDIVIDUAL INT
    print("/n")
    pprint(ints)
    print("/n")
    print("Interface {}: inOctet = {} AND outOctets = {}".format('Ethernet2', inOct, outOct))
    print("/n")
    # example with Ethernet2
    inOct = r_ints[0]['result']['interfaces']['Ethernet2']['interfaceCounters']['inOctets']
    outOct = r_ints[0]['result']['interfaces']['Ethernet2']['interfaceCounters']['outOctets']
    print("inOct = {} and outOct = {}".format(inOct, outOct)
    # pprint(r_ints)



def main():
    # create a node object by specifying the node to work with
    node = pyeapi.connect_to('pynet-sw3')

    # send one or more commands to the node
    r_ints = node.enable('show interfaces')

    # disects result ints (r_ints) and saves the first element in list, 
    # then results and interfaces keys.
    ints = r_ints[0]['result']['interfaces'] 


    # tshoot(r_ints, ints)

    for int, value in ints.items():
        # if ints.get(int)
        if value.get(int)
            pprint("starting interface: {}".format(int))
            int_counters = value.get('interfaceCounters', {})
            inOct  = int_counters.get('inOctets')
            outOct = int_counters.get('outOctets')
            # inOct  = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['inOctets']
            # outOct = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['outOctets']
            print("Interface {}: inOctet = {} AND outOctets = {}".format(int, inOct, outOct))
        else:
        	print("Interface {} does not report in/out Octets".format(int))

## Old way... not versitile
    # for int, value in ints.items():
    #     if int == 'Vlan1':
    #         continue
    #     else:
    #         pprint("starting interface: {}".format(int))
    #         inOct  = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['inOctets']
    #         outOct = r_ints[0]['result']['interfaces'][int]['interfaceCounters']['outOctets']
    #         print("Interface {}: inOctet = {} AND outOctets = {}".format(int, inOct, outOct))


    # this interfaces var is currently not what I need (used 'ints' above instead)
    # interfaces = result[0]['result']['interfaces'].keys()
    # I could have used this as it turns out by casting this to a list like this...
    # interfaces = list(result[0]['result']['interfaces'].keys())

	# not working due to interfaces being a class... 
	# and I can't figure out how to access the list contained within
	#for int in interfaces:
	#     inOct = result[0]['result']['interfaces'][{int}]['interfaceCounters']['inOctets']
	#     outOct = result[0]['result']['interfaces'][{int}]['interfaceCounters']['outOctets']
	#     print("Interface {}: inOctet = {} AND outOctets = {}".format(int, inOct, outOct))  



if __name__ == "__main__":
    main()

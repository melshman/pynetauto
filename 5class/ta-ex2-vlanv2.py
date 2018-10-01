#!/usr/bin/env python

"""
2. Using Arista's pyeapi, create a script that allows you to add a VLAN 
(both the VLAN ID and the VLAN name).  

Your script should first check that the VLAN ID is available and only 
add the VLAN if it doesn't already exist.  Use VLAN IDs between 100 and 999.  You should be able to call the script from the command line as follows:

   python eapi_vlan.py --name blue 100     # add VLAN100, name blue

If you call the script with the --remove option, the VLAN will be removed.

   python eapi_vlan.py --remove 100          # remove VLAN100

"""


#import pyeapi
from pprint import pprint
import argparse
from getpass import getpass
import sys
import pyeapi

# def testing(args_list):
#     print(args_list)
#     for arg in args_list:
#         print("Argument:  {}".format(arg))
    
#     if args_list[1]:
#         a1 = args_list[1]
#         print(a1)
#         print(type(a1))

#     if args_list[1]:
#         a2 = args_list[2]
#         print(a2)
#         # a2=int(a2)
#         print(type(a2))

def test_vlan():
    # return all vlans from the node
    vlans.getall()

    # return a specific vlan from the node
    vlans.get(1)

    # add a new vlan to the node
    vlans.create(100)
    vlans.set_name(100, "blue")
    vlans.delete(100)
    # create name  
    # vlans.configure_vlan(blue)

def main():
    args_list = sys.argv
    # testing(args_list)

    # create a node object by specifying the node to work with
    node = pyeapi.connect_to('pynet-sw3')

    # get the instance of the API (in this case vlans)
    vlans = node.api('vlans')
    # test_vlan()
    vlan_list = vlans.getall()
    vlan_ids = list(vlan_list.keys())

    if args_list[1] == "--name": # add vlan operation
        if len(args_list) != 2:
            print ("--name function detected, but invalid arguments passed to script.  Boycott in effect!")
        elif args_list[2] not in vlan_ids:
            vid = args_list[3]
            vname = args_list[2]
            vlans.create(vid)
            vlans.set_name(vid, vname)  
            print("vlan added!  ID: {} , Name: {}".format(vid, vname))
    if args_list[1] == "--remove": # add vlan operation
        if len(args_list) < 2:
            print ("--remove function detected, but invalid arguments passed to script.  Boycott in effect!")
        elif args_list[2] in vlan_ids:
            args_list.pop(0)
            args_list.pop(0)
            # print(args_list)
            for arg in args_list:
                vlans.delete(arg)
                print("removed vlan id {}".format(arg))
                # add code to actually remove the vlans
        else:
            print("VLAN does not exist and thus can't be removed!") 
    else:
        print ("Invalid arguments passed to script.  use --name or --remove")

if __name__ == '__main__':
    main()

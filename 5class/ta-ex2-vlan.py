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


def main():
    args_list = sys.argv
    # testing(args_list)

    if args_list[1] == "--name": # add vlan operation
        print("This function will add a vlan with id {} and name {}".format(args_list[3], args_list[2]))


    if args_list[1] == "--remove": # add vlan operation
        args_list.pop(0)
        args_list.pop(0)
        print(args_list)
        for arg in args_list:
            print("remove vlan id {}".format(arg))
            # add code to actually remove the vlans


if __name__ == '__main__':
    main()

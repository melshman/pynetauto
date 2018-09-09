#!/usr/bin/env python
"""
Write a Python program using ciscoconfparse that parses the 'cisco_ipsec.txt'
config file. Note, this config file is not fully valid (i.e. parts of the
configuration are missing).

The script should find all of the crypto map entries in the file (lines that
begin with 'crypto map CRYPTO') and print out the children of each crypto map.
"""
from __future__ import unicode_literals, print_function
from ciscoconfparse import CiscoConfParse
from printout import printout

def main():
    """
    Find all of the crypto map entries in the file (lines that begin with
    'crypto map CRYPTO') and print out the children of each crypto map.
    """
    cisco_file = 'cisco_ipsec.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    printout(cisco_cfg)
    
    crypto_maps = cisco_cfg.find_objects(r"^crypto map CRYPTO")
    printout(crypto_maps)
    print("\n")

    for c_map in crypto_maps:
        print()
        print(c_map.text)
        for child in c_map.children:
            print(child.text)
    print("\n")


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
from __future__ import unicode_literals, print_function
import json
import yaml
from pprint import pprint


def main():
    my_list = [
    	'cisco', "juniper", {"users":{"username":"john", 
    	"password":"password123"}},"nexus", {"vlans":{"vlan_name":"vlan22", "vlan_id":"22"}}, "HP"]
    print(my_list)
    print(my_list[0])
    print(my_list[2].keys())
    print(my_list[2].values())
    print(my_list[2]["users"].keys())
    print(my_list[2]["users"].values())
    print(my_list[2]["users"]['username'])
    print(my_list[2]["users"]['password'])
    print("\n")

    with open('data.yml', 'w') as outfile:
    	yaml.dump(my_list, outfile, default_flow_style=False)

    with open('data.json', 'w') as outfile:
        json.dump(my_list, outfile)

    with open('data.json','r') as f:
        json_data = json.load(f)	

    pprint(json_data)
    print("\n")

    with open('data.yml','r') as f:
        yaml_data = yaml.load(f)

    pprint(yaml_data)

if __name__ == "__main__":
	main()

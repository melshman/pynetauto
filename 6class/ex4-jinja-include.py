#!/usr/bin/env python


"""
The main template should be stored in an external file named 'arista_template.j2'. 

This template should use the Jinja2 include statement to pull in two additional templates. 
The first template should be named 'arista_users.j2' and should contain the two username 
statements. The second template should be named 'snmp.j2' and should include all of the 
SNMP statments.

The SNMP location, contact, and community should all be made into Jinja2 variables. 
The rest of the configuration can be hard-coded (i.e. you don't need any other variables 
besides those three SNMP variables).
"""


from __future__ import unicode_literals, print_function
# from jinja2 import FileSystemLoader, StrictUndefined
# from jinja2.environment import Environment
import jinja2
from getpass import getpass


#  SNMP location, contact, and community 
snmp_vars = {
    'snmp_location': 'Isaac Newton',
    'snmp_contact': 'San Francisco, CA',
    'snmp_community': 'foo'
}


def main():
    env = jinja2.environment.Environment(undefined=jinja2.StrictUndefined)
    env.loader = jinja2.FileSystemLoader('.')
    template_file = 'arista_template.j2'
    template = env.get_template(template_file)
    output = template.render(**snmp_vars)
    print(output)

if __name__ == '__main__':
    main()

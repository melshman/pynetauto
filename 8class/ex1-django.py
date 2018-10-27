#!/user/bin/env python

from __future__ import print_function
from __future__ import unicode_literals

from getpass import getpass
from pprint import pprint



'''
1. Initialize your Django database. Add the seven NetworkDevice objects 
and two Credentials objects into your database. After this initialization, 
you should be able to do the following (from the ~/DJANGOX/djproject directory):

$ python manage.py shell

>>> from net_system.models import NetworkDevice, Credentials
>>> net_devices = NetworkDevice.objects.all()
>>> net_devices
[<NetworkDevice: pynet-rtr1>, <NetworkDevice: pynet-sw1>, <NetworkDevice: pynet-sw2>, 
<NetworkDevice: pynet-sw3>, <NetworkDevice: pynet-sw4>, <NetworkDevice: juniper-srx>, 
<NetworkDevice: pynet-rtr2>]

>>> creds = Credentials.objects.all()
>>> creds
[<Credentials: pyclass>, <Credentials: admin1>]


    b. Update the NetworkDevice objects such that each NetworkDevice links to the correct Credentials.

    '''

def main():
	

if __name__ == 'main':
	main()


###
###

### !usr/bin/env python
from pprint import pprint

def printout(var):
	# var.name()
	banner = '-' * 80
	# print(var.name)
	print(banner)
	pprint(var)
	print(banner)
	print(type(var))
	# print(name(var))
	print("\n" *2)	
	return
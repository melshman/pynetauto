#!/usr/bin/env python

from __future__ import print_function, unicode_literals

'''

1. Create a directory called mytest. In ./mytest create three Python modules world.py, 
simple.py, whatever.py.

     a. These three files should each have a function that prints a statement when 
     called (func1, func2, func3).
     b. In each of the three modules use the __name__ technique to separate executable 
     code from importable code. Each module should contain executable code.
     c. Verify that you are NOT able to 'import mytest' (try this from the directory 
     that contains ./mytest).

Note, recent versions of Python3 will allow you to import the package even though 
no __init__.py exists in the directory. In other words, recent versions of Python3 
(Python3.3 or greater) will allow packages without __init__.py files in certain contexts.


'''

def simple_func1():
	print('This is func1 from simple.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def simple_func2():
	print('This is func2 from simple.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def simple_func3():
	print('This is func3 from wsimple.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def main():
	print('\nYou just ran simple.py directly as a main script.')
	print('The name of the __name__ variable is {}!'.format(__name__))
	

if __name__ == "__main__":
	main()

print("Just a simple hello")
#!/usr/bin/env python
from mytest import *

def main():

	my_hello = MyClass("Mr.", "Tim", "Armstrong")
	my_hello.hello()
	my_hello.not_hello()
	print("\n")
	# print("This is the directory for {}:\n".format(my_hello, dir()))

	french_hello = FrenchClass("Mrs.", "Juyong", "Armstrong")
	french_hello.hello()
	print("\n")

	doggie_hello = FrenchClass("Mrs.", "Juyong", "Armstrong", "Mando")
	doggie_hello.hello()
	print("\n")


if __name__ == "__main__":
	main()
#!/user/bin/env python

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

4. Create a class MyClass in world.py.

    a. This class should require that three variables be passed in upon initialization.
    b. Write two methods associated with this class 'hello' and 'not_hello'. 
    Have both these methods print a statement that uses all three of the initialization 
    variables.


5. Write a child class MyChildClass of MyClass. This child class should override 
the 'hello' method and print a different statement.


6. Optional bonus question -- have MyChildClass augment the __init__() method. 
In other words, the child class should do something additional in the __init__() 
method yet still call its parent class __init__().

'''

def world_func1():
	print('This is func1 from world.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def world_func2():
	print('This is func2 from world.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def world_func3():
	print('This is func3 from world.py!')
	print('The name of the __name__ variable is {}!'.format(__name__))


def main():
	print('\nYou just ran world.py directly as a main script.')
	print('The name of the __name__ variable is {}!'.format(__name__))
	
	my_hello = MyClass("Mr.", "Tim", "Armstrong")
	my_hello.hello()
	my_hello.not_hello()
	# print("This is the directory for {}:\n".format(my_hello, dir()))

	french_hello = FrenchClass("Mrs.", "Juyong", "Armstrong")
	french_hello.hello()

	doggie_hello = FrenchClass("Mrs.", "Juyong", "Armstrong", "Mando")
	doggie_hello.hello()


class MyClass(object):
	def __init__(self, sex, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.sex = sex

	def hello(self):
		print("Hello {} {} {}, how are you today?".format(self.sex, self.first_name, self.last_name))

	def not_hello(self):
		print("Not going to say hello you to this morning, {} {} {}, because you are an terd!".format(self.sex, self.first_name, self.last_name))


class FrenchClass(MyClass):
	### modify the main class __init__ function ---- Add statement #####
	def __init__(self, sex, first_name, last_name):
		print("Welcome to {} __init__ function!".format(FrenchClass))
		MyClass.__init__(self, sex, first_name, last_name)


    ### Alternative Version ---- Add a new variable argument
	def __init__(self, sex, first_name, last_name, dog_name=None):
		if not dog_name:
			MyClass.__init__(self, sex, first_name, last_name)
			self.dog_name = dog_name
			print("Dog name is {}.".format(self.dog_name))
		else:
			MyClass.__init__(self, sex, first_name, last_name)
			self.dog_name = dog_name
			print("Dog name is {}.".format(self.dog_name))

	def hello(self):
		if not self.dog_name:
			print("Bonjour! {} {} {}!  How are you today?".format(self.sex, self.first_name, self.last_name))
		else:
			print("Doggie Dog Welcome to you, {} {} {}, and your doggie, {}!".format(self.sex, self.first_name, self.last_name, self.dog_name))


if __name__ == "__main__":
	main()

print("Hello from world.py")
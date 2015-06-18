#!/usr/bin/python -tt

'sd;kvngfidsvbofdmbp'
import sys
import time
import abc

class Employee:
	__metaclass__ = abc.ABCMeta
	
	def __init__(self):
		print ('entering the default constructor of the base class')
	
	@abc.abstractmethod
	def calculateSomething(self, a, b):
		print('Entering the calculateSomething method in the base class')
		

class BlueBadgeEmployee(Employee,object):
	
	def __init__(self):
		super(BlueBadgeEmployee, self).__init__()
		print('entering the default constructor of the BlueBadgeEmployee child class')
		
	def calculateSomething(self, a, b):
		self.a = a
		self.b = b
		super(BlueBadgeEmployee, self).calculateSomething(a,b)
		print('entering the calculateSomething method of the BlueBadgeEmployee child class')
		print('Here we do addition')
		return (a+b)
		
class GreenBadgeEmployee(Employee):
	
	def __init__(self):
		print('entering the default constructor of the GreenBadgeEmployee child class')
		
	def calculateSomething(self, a, b):
		print('entering the calculateSomething method of the GreenBadgeEmployee child class')
		print('Here we do multiplication')
		return (a*b)
		
# Define a main() function that prints a little greeting.
def main():
	# Get the name from the command line, using 'World' as a fallback.
	emp = Employee()
	#emp.calculateSomething()
	emp = BlueBadgeEmployee()
	emp.calculateSomething(2,3)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
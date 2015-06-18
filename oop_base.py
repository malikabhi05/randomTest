#!/usr/bin/python -tt

'sd;kvngfidsvbofdmbp'
import sys
import time
import abc

class Employee:
	'this is a test class and .... lets play'
	
	empCount = 0
	__secretCount = 0
	
	def __init__(self):
		print('this is the default constructor of the parent class')
	
	def __init__(self, name, salary):
		print('this is the constructor in the parent class')
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		Employee.__secretCount += 1
		
	def printEmployeeDetails(self):
		print ("Employee Name: "+self.name+" Salary: "+str(self.salary))
		
	def printRandom(self):
		print('this is a random function')

	def getSecretCount(self):
		print('secre count inside the getSecretCount function: '+str(Employee.__secretCount))
		return self.__secretCount
		
	def extraMethod(self):
		print('this is the extraMethod in the parent class')
		
	#def __del__(self):
		#className = self.__class__.__name__
		#print('Name of the class being destroyed is: '+className)


class GreenBadgeEmployee(Employee,object):
	def __init__(self):
		super(GreenBadgeEmployee, self).__init__('ya',20000)
		print('this is the constructor of the child class')
	
	def extraMethod(self):
		print('this is the extraMethod in the child class')
		
# Define a main() function that prints a little greeting.
def main():
	# Get the name from the command line, using 'World' as a fallback.
	emp1 = Employee('abhishek',10000)
	emp2 = Employee('********',10000)
	emp1.printEmployeeDetails()
	emp2.printEmployeeDetails()
	print('the total number of employees added is: '+str(Employee.empCount))
	#print('the total number of secrets: '+str(Employee.__secretCount))
	print('Doc: '+Employee.__doc__)
	print('Name: '+Employee.__name__)
	print('Module: '+Employee.__module__)
	print('Bases: '+str(Employee.__bases__))
	print('Dict: '+str(Employee.__dict__))
	gbemp1 = GreenBadgeEmployee()
	gbemp1.extraMethod()
	emp1.extraMethod()
	emp1 = gbemp1
	emp1.extraMethod()
	gbemp1.printRandom()
	print('accessing a parent class variable using a child class object: '+str(gbemp1.empCount)+' name: '+gbemp1.name)
	print('printing the secret count value outside: '+str(emp2._Employee__secretCount))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
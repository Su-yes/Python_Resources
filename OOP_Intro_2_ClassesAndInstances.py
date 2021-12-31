# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 21:15:23 2020

@author: bhatt
"""

'''
Methods are just functions associated with a class. 

Class is a blueprint for creating instances. 

Each object you create using a class is an instance of the class. 

'''
class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def get_info(self):
        print(f'''\
              name = {self.first} {self.last}
              pay = {self.pay}
              email = {self.first}.{self.last}@acompany.com
              ''')
e1 = Employee("Suyash", "Bhattarai", 2000)
e2 = Employee("Suku", "Bhattarai", 3000)


e2.get_info()
Employee.get_info(e2)

'''
In the first line, since you are already calling a method on an specific insntance( (e2), you do not need to pass anything in the ()
                                                                                   
In the second line, since you are just calling on the methond of the class Employee, you need to pass an instance. 

Executing the first line basically executes the second line where it passes the e2 automatically, so you need the "self" in the method as a placeholder to accept the instance. 
'''
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:43:26 2020

@author: sbhatta8
"""
class Employee:
    
    raise_amount = 1.04 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@acompnay.com"
        
        
    def fullname(self):
        print(f"{self.first} {self.last}")
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    '''
    Just like how a method accepts an instance and modifies the instance attributes, class method accpets class 
    often writen as "cls" and modifies or sets the class varriables
    '''
    
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
        # Your are calling the class with this return statement
    
e1 = Employee("Suyash", "Bhattarai", 1000000)
e2 = Employee("Suku", "Bhattarai", 35000)

# Before and after
print(Employee.raise_amount) 
Employee.set_raise_amount(1.05)
print(Employee.raise_amount) 
print(e1.raise_amount)
print(e2.raise_amount)
print(e1.pay)

#  You can run a class method from an instance like so but no really does this
print("\n")
print(Employee.raise_amount) 
e1.set_raise_amount(1.10)
print(Employee.raise_amount) 
print(e1.raise_amount)
print(e2.raise_amount)

# ---------------------------------------------------------
e1_str = "Suyash-Bhattarai-25000"
e2_str = "Sukrit-Bhattarai-85000"

new_e1 = Employee.from_string(e1_str)

print(new_e1.email)
print(new_e1.pay)


#-------------------------------
'''
Static method don't take any instance or class as default argument. 
They are in a class becuase it makes sense logcially. 

'''
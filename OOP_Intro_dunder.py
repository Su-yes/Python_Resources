# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 15:56:18 2022

@author: bhatt
"""

class Employee:
    
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@acompnay.com"
                
    def fullname(self):
        return f"{self.first} {self.last}"
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
    
        
    '''
    Help other developer understand what the object is. 
    At least have an __repr__ bc if there isn't a __str__, it defaults to __repr__'
    
    Try to display something that you can copy and paste back in python to create the same object. 
    '''
    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})"
        
    '''
    Help end user understand what the object is. 
    ''' 
    def __str__(self):
        # return f"{self.fullname()} - {self.email()}"   
        return f"{self.fullname()} - {self.email} "


    # Additional special methods example
    def __add__(self, other):
        return self.pay + other.pay

    
    def __len__(self):
        return len(self.fullname())




e1 = Employee("Suyash", "Bhattarai", 1000000)
e2 = Employee("Suku", "Bhattarai", 35000)

print(e1) # prints a info about the employee. What it is depends on __repr__ method

# the above statement is actually calling. 
print(e1.__repr__())
print(e1.__str__())

# You get the exact same thing. 

# =============================================================================
# 

print(1+2)
# What it's actually doing in the background
print(int.__add__(1,2))

# Example
print(e1+e2)


print(len("Sushi"))

print(str.__len__("sushi"))


print(len(e2))
# =============================================================================

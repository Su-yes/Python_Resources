# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 21:20:22 2022

@author: bhatt
"""

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = first + "." + last + "@acompnay.com"
    
    @property            
    def fullname(self):
        return f"{self.first} {self.last}"
    
    @property
    def email(self):
        return f"{self.first}.{self.last}@company.com"
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print("Name Deleted!!")
        self.first = None
        self.last = None

e1 = Employee("Suyash", "Bhattarai", 1000000)
e2 = Employee("Suku", "Bhattarai", 35000)

e1.first = "Bob"
e1.fullname = "bhatte asdf"

print(e1.first)
print(e1.email)
print(e1.fullname)

del e1.fullname
print(e1.fullname)


'''Property allows you to define a method like an attribute. 

We are defining our email like a method but we can access it like an attribute. This is helpfull when you don't wnat to change the code because someone might be using it'
'''
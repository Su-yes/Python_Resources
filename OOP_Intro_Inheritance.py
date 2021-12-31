# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:29:07 2020

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

class Developer(Employee):
    raise_amount  = 1.06
    
    def __init__(self, first, last, pay, lang):
        super().__init__(first, last, pay)
        self.lang = lang
    
class Manager(Employee):
    
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
 
    def remove_emp(self, emp):           
        if emp in self.employees:
            self.employees.remove(emp)
        
        
# e1 = Employee("Suyash", "Bhattarai", 1000000)
# e2 = Employee("Suku", "Bhattarai", 35000)

e1 = Developer("Suyash", "Bhattarai", 1000000, "Python")
e2 = Developer("Suku", "Bhattarai", 35000, "Java")

print(e1.lang)
print(e2.lang)

e3 = Manager("Jason", "Bhattarai", 5000, ["Phill", "David"])
e4 = Manager("Mitch", "Bhattarai", 2000, ["Tyler", "Heath", "Kyle"])

print(e3.employees)
print(e4.employees)

e3.add_emp("Conner")

print(e3.employees)
print(e4.employees)

e4.remove_emp("Tyler")
print(e3.employees)
print(e4.employees)

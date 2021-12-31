class Employee:
    
    raise_amount = 1.04
    
    # This is class varriable. It is the same for every instance. 
    # You need to access them through the class itself or an instnace of a class. 
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@acompnay.com"
        
        # These above varriables are called instnace varriables as they can varry among the instances.
        
    def fullname(self):
        print(f"{self.first} {self.last}")
        
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        # or, 
        # self.pay = int(self.pay * self.raise_amount) # access through class or instance
        # This gives you the ablity to change ther raise for single instance

e1 = Employee("Suyash", "Bhattarai", 1000000)
e2 = Employee("Suku", "Bhattarai", 35000)

e1.fullname()
Employee.fullname(e2)
print(e1.email)

print(e1.pay)
e1.apply_raise()
# access them through the class itself or an instance of a class.
# Python checks the instnace first for the attribute and if not found, searches the class. 
print(Employee.raise_amount) 
print(e1.raise_amount)
print(e2.raise_amount)
print(e1.pay)

# search attributes
print(e1.__dict__)
# no raise_amount

print(Employee.__dict__)
# Raise_amount present

# Change the class varriable
Employee.raise_amount = 1.05

print(e1.pay)
e1.apply_raise()
# access them through the class itself or an instance of a class.
# Python checks the instnace first for the attribute and if not found, searches the class. 
print(Employee.raise_amount) 
print(e1.raise_amount)
print(e2.raise_amount)
print(e1.pay)


# Change class varriable for just one instance
e1.raise_amount = 1.10
print(Employee.raise_amount) 
print(e1.raise_amount)
print(e2.raise_amount)

''' 
line 61 does just change the raise amount value; it creates the raise amount attribute for employee 1. 
'''
# check
print(e1.__dict__)

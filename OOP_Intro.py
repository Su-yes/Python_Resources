# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 21:44:53 2020

@author: bhatt
"""

x = "1"
print(type(x))

def hello():
    print("Hello")
print(type(hello))

'''
String and int are part of a class.
x is equal to the object which is a type interger with a value 1.
Pretty much everything in python is an object of some class.
Whenenever you are creating something in Python, you are creating and object which is an instance of a class.  

'''

string  = "Hello"
print(string.upper())

'''
Method acts on a specific object. 
In this case, .upper() is a method that acts on an object of type string stored in "string"

'''
    
class Dog: 
        
    def bark(self):
        print("Bark")
    
    def add_one(self, x):
        return x + 1
        
d = Dog() 
'''
Create a varriable d and assign it to an instnace of class dog. 
You are instantiating or creating a new instance of class dog.
'''
 # verify
print(type(d)) 

'''
bark is a method. 
You can use the method on an instance of class by doing
'''
d.bark()
print(d.add_one(6))

'''
__init__ allows us instantiate and object right when it is created. This method will be immediately called when ever you create an object (an instance of a class).    
'''

class DogTow: 
    
    def __init__(self, name):
        self.dogname = name
    
    def get_name(self):
        '''We need to add slef to invisibly pass which does we want the name for'''
        print(self.dogname)
        
    #  You can also modify the attributes using method
    def set_name(self, name):
        self.dogname = name
        

'''
dog name is an attribute of the object.
Stored permanentely for each object
'''

e = DogTow("Charlie") # automatically passes "Charlier" when creating an instance
print(e.dogname)

f = DogTow("Murphy")
print(f.dogname)

e.get_name()
f.get_name()

'''
Here, no need to pass the dog inside the () because when you call the method on the object e or f, the object invisibly get passed on to the method.
'''

f.set_name("Murphy Modified")
f.get_name()


# An Example

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            print("Added")
        else:
            print("Not Added")
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        
        return value / len(self.students)
    
s1 = Student("Sushi", 23, 95)
s2 = Student("Suku", 59, 23)
s3 = Student("Ryan", 18, 65)
s4 = Student("Jason", 19, 85)


course1 = Course("Algebra", 2)
course1.add_student(s1)
course1.add_student(s2)
course1.add_student(s3)
# course1.add_student(s3)

print(course1.get_average_grade())

# Inheritance 
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

class Fish(Pet):
    
    def __init__(self, name, age, color):
        '''use super() to call the parent method so important initializations are take care off'''
        super().__init__(name, age)
        self.color  = color
        
    def speak(self):
        print("Meow")
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")       

class Dog(Pet):
    def speak(self):
        print("Bark")
        
class Cat(Pet):
   def speak(self):
       print("Meow")       

            

s = Pet("Timber", 14)
s.show()

x = Cat("Bill", 24)
x.show()

y = Dog("Jill", 88)
y.show()

'''
Even though show() is not defined specifically for Cat and dog, it still works because it inherits the method from the parent class. 

speak method however is defined for each class so it will work as expected
'''

x.speak()
y.speak()


z = Fish("Nemo", 2, "Orange")
z.show()

# Class varriables and decorators

class Person:
    number_of_people = 0
    GRAVITY = -9.8
    
    def __init__(self, name):
        self.name = name
        Person.add_person()
    
    @classmethod
    def number_of_people_(cls):
            return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Suyash")
# print(Person.number_of_people())
p2 = Person("Suku")
# print(Person.number_of_people())

print(Person.number_of_people_())


# Static Method
class Math:
    
    @staticmethod
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 10
    
print(Math.add10(20))

'''
When I started learning OOP it took me a while to differentiate between methods types, so if you are struggling with that too, here's a quick summary:

Method = function related to that instance of a class. Use this type it when you are using values of the own instance (its own name, age, etc). You need to create one instance to use it.

Classmethod = function related to that class and that class only. Use this type when you are using values of the class, not the instance (For example, using a class that retrieves the total count of instances of that Class created and stored in a class variable). You don't need to create one instance to use it.

Staticmethod = function not related to that class. Used for organization purposes (For example, a Calculator class with add, subtract, multiplicate, etc methods). You don't need to create one instance to use it.
'''





















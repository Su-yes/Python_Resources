#%%
'''Real numbers vs integers'''

'''Integers are called int and written as 23. Real numbers are called float and have decimal points, like 23.0.

// is called floor division and returns and interger '''

a = 23//2 #11

'''but 23//2.0 returns a float so be careful.'''
b = 23//2.0 #11.1

'''You can ensure a nubmer a is float or int by doing the follwoing:'''

c = int(3) #3
d = float(4) #4.0
e = float(23)//2 #11.5
f = int(23)//2 #11

'''float() and int() can be used to convert numbers too!'''

'''Other Operations
x % y = remainder
x ** y gives x^y
round()-> round the float x, to the nearest whole. Always results in an int. 
abs(x)-> Return the absolute value. 
'''

#%%
'''Strings are a sequence of characters'''
name = 'Suyash Bhattarai'
print("My name is ", name)
print(name[0]) #prints s
name2 = "Suyash" + "Bhattarai"
print("My new name is", name)

'''You can convert an integer to a string'''
g = str(23)
print(g[0])
print(g[1])
h = int(g)
print(h)

#%% Getting Input
'''name = input("Please enter you name")
print("The name you entered isbob",name)

age = int(input("Please enter your age:"))
olderAge = age + 1
print ("Next year you will be", olderAge)'''
#%%
'''Defining Functions'''
# the colon indicates that the next line of code will be indented and controlled by the function. Def in this case
def g(x):
    return x**4/4.0-x**3/3.0-3*x*x
print(g(18))

#%%
'''Reserved words'''
print("\n")
import keyword
print(keyword.kwlist)

#%% 
'''Dot Notation'''
print("\n")
from datetime import date
mydate = date.today()
print(mydate.year)
print(mydate.month)
print(mydate.day)

#%%
print("\n")
'''Conditionals and control structures'''
'''If statements must have indentation'''
mynum1 = 3
mynum2 = 2
if mynum1>mynum2:
    print("it works")
print("completed")

'''Vriables inside a control struutres cannot be accesed after the control structure'''


#in for loop the values of the iterrator doesn't change.
print("\n")
for i in range(1,5):
     print("Before:",i)
     i += 1
     print("After adding 1:",i)
     
#%%
'''For-each loops'''
print("\n")
num = [10,20,30,40,50,60,100]
sum=0
for currentnum in num:
    sum += int(currentnum)
    
print(int(sum/len(num)))
    
#%% 
'''While loop'''
print("\n")
i=1
while i<11:
    print(i)
    i += 1
    
#%% 
#must define a fucntion before you use it.     
print("\n")
#defines the fucntion "printdollar"
def printdollar():
    #prints "$" without the new line afterward
    print("$", end="") 
    
#calls the fucntion "printdollar"
printdollar() #just prints the dollar and doesn't got the next line
print(7) #Then prints 7


print("\n")
#defines the fucntion "printdollar"
def returndollar():
    return "$"

print(returndollar(),end="")
print(5)


print("\n")
#defines the fucntion "printdollar"
def returndollaramt(x):
    return "$"+str(x)

print(returndollaramt(99))

#%%
print("\n")
'''Get rid of spaces and new lines'''

print("A","B","C")
print("D","E","F")
print("A","B","C",sep="",end="")
print("D","E","F",sep="",end="")
print("A","B","C",sep="$",end="#")
print("D","E","F",sep="?",end="!")


#%% Error handling
print("\n")
mystring = "lol"

try:
    print("Convert to an integer...")
    myint = int(mystring)
    print(myint)
#if an error occurs, jump to here    
except:
    pass
print("Done!")

print("\n")
mystring = "lol"

try:
    print("Convert to an integer...")
    myint = int(mystring)
    print(myint)
#if an error occurs, jump to here    
except:
    print("Can't convert a string to a number")
print("Done!")

'''
print("\n")
mystring = "lol"

try:
    print("Convert to an integer...")
    print("String #" + 1 + ":" + mystring)
    myint = int(mystring)
    print(myint)
#if a value error occurs jump to there 
except ValueError:
    print("Can't convert a string to a number")
print("Done!")
'''



print("\n")
mystring = "lol"

try:
    print("Convert to an integer...")
    myint = int(mystring)
    print(myint)
#if an valueerror occurs, jump to here    
except ValueError as error:
    print(error)
print("Done!")

#%%
# printing the memory address
print("\n")
xxx = 25
print(id(xxx))

#%% Special characters

print('\n')
print('12345\n678\t789\\lol')

print('\n')
rip = 'abcdefg'
start=0
end = 3
print('first three character: ' + rip[start:end])

print(rip[:3])
print(rip[3:])

print(rip[:-2])
print(rip[-2:])

print(rip.find('cd'))


# can also provide parameters for find method find('text',2,3)


'''don't forget the split commnad too'''

#Tupple are immutable











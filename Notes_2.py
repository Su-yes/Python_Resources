# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:33:50 2020

@author: sbhatta8
"""

# Numbers
print(17 / 3)  # division always returns a floating point number
print(17 // 3) # floor division discards the fractional part
print(17 % 3) # returns the remainder

# Strings

# In interactive mode, the last printed expression is assigned to the variable _

'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead

# If you don’t want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote:

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# note that the initial newline is not included because of \
print('Py' 'thon') # automatically

text = ('Put several strings within parentheses '
     'to have them joined together.')
print(text) # Another example

# This only works with two literals though, not with variables or expressions

word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5
word[-1]  # last character
word[-2]  # second-last character
word[-6]
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

# How strings are indexed. The indices as pointing between characters, with the left edge of the first character numbered 0. 
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6  Positive index
#-6  -5  -4  -3  -2  -1      Negative index

# Python strings cannot be changed — they are immutable. 

s = 'supercalifragilisticexpialidocious'
print(len(s))

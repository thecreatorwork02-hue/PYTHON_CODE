import string
from tkinter import FALSE


a = 21 #interger
b = 54.54 #float
c = "hyyy" #string
d = True #boolean, 
e = None #none  
print (a)
print (b)
print (c)                   
print (d)
print (e)
#Invalid variable names
# 1name = "John"  # starts with a number
# name-with-dash = "John"  # contains a dash
# n ame with space = "John"  # contains a space
# @name = "John"  # contains a special character


print(type(a))  # Check and display the variable's type
c = str(a)
print(c)
# Convert a to a string
text = str(input("enter your name: ")) #to take input from user


#OPERATIONS 
#ARTHIMETIC OPERATIONS
x = 10
y = 3
print(x + y)  # Addition
print(x - y) # Subtraction
print(x * y) # Multiplication
print(x / y) # Division

#ASSINGMENT OPERATIONS
a = 5
a+= 3  # Equivalent to a = a + 3
print(a)  # Output: 8

#COMPARISON OPERATIONS
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to


#LOGICAL OPERATIONS
p = True
q = False
print(p and q)  # Logical AND

#TRUTH AND FALSE TABLE FOR OR 
print("True or False is" , True or False)  # Logical OR
print("True or True is" , True or True)  # Logical OR
print("False or True is" , False or True)  # Logical OR
print("False or False" , False or False)   #Logical OR


#TRUTH AND FALSE TABLE FOR AND
print("True and False is" , True and False)  # Logical OR
print("True and True is" , True and True)  # Logical OR
print("False and True is" , False and True)  # Logical OR
print("False and False" , False and False)   #Logical OR

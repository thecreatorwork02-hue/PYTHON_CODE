a = "Divanshu" #String
# for string positive indexing starts from 0
# negative indexing starts from -1
w = a[0:5] #Slicing
x = a[0:9:2] #Slicing with step
print(w)
print(x)
# String Functions
print(len(a)) #Length of string
print(a.upper()) #Convert to uppercase
print(a.lower()) #Convert to lowercase
print(a.replace("v", "b")) #Replace character
print(a.split("v")) #Split string based on character
print(a.find("n")) #Find index of character
print(a.count("u")) #Count occurrences of character
print(a.capitalize()) #Capitalize first letter
print(a.count("a")) #Count occurrences of character


#Escape Characters
print("Hello\nWorld") #New line
print("Hello\tWorld") #Tab
print("Hello\\World") #Backslash
print("Hello\"World\"") #Double quote
print("Hello\'World\'") #Single quote
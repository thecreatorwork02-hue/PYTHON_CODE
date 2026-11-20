list = [1, 2, 3, 4, 5,6] #List
list[2:4] #Slicing
list[0:6:2] #Slicing with step
print(list[2:4])
print(list[0:6:2])
# List Functions
print(len(list)) #Length of list    
print(list.append(6)) #Add element to end of list
print(list.insert(0, 0)) #Add element at specific index 
print(list.remove(3)) #Remove element by value
print(list.pop()) #Remove last element  
print(list.sort()) #Sort list
print(list.reverse()) #Reverse list
print(list.count(2)) #Count occurrences of element  
print(list.index(4)) #Find index of element
print(list.clear()) #Clear list

# Tuple
tuple = (1, 2, 3, 4, 5) #Tuple
print(tuple[0:3]) #Slicing
print(tuple[0:5:2]) #Slicing with step  
# Tuple Functions
print(len(tuple)) #Length of tuple
print(tuple.count(2)) #Count occurrences of element
print(tuple.index(4)) #Find index of element

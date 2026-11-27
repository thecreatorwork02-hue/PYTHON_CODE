a = {"name": "John", "age": 30, "city": "New York"}   #dictionary
print(a["name"])   #accessing value using key


# Dictionary Methods
a.items()   #returns a list of tuples containing key-value pairs
a.keys()    #returns a list of keys in the dictionary
a.update({"country": "USA", "age": 35})   #adds a new key-value pair to the dictionary or update the old pair
a.get("name")   #returns the value associated with the key "name"
print(a)   #prints the updated dictionary


#Difference between a["age2"] and a.get("age2")
#print(a["age2"])  #give error if key is not present in dictionary
#and 
#print(a.get("age2")) #give None if key is not present in dictionary

set1 = {1, 2, 3}   #set
set2 = {3, 4, 5}   #another set
empty_set = set()  #empty set
print(type(empty_set))   #prints <class 'set'>

# Set Methods
set1.add(4)   #adds an element to the set
set1.remove(2)   #removes an element from the set
set1.union({5, 6})   #returns a new set that is the union of set1 and another set
set1.intersection({3, 4, 5})   #returns a new set
set1.clear() # empty the set 
set1.issubset({1, 3, 4})   #returns True if set1 is a subset of another set
print(set1)   #prints the updated set
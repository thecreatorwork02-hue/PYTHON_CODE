a = int(input("Enter Marks of Subject 1: "))
b = int(input("Enter Marks of Subject 2: "))
c = int(input("Enter Marks of Subject 3: "))

d = ((a+b+c)/300)*100

print("Your percentage is: ", d)

if(d>=40 and a>=33 and b>=33 and c>=33):
     print("You are pass.")

else:
     print("You are fail.")
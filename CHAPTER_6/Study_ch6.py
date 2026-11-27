a = int(input("Enter your age: "))
#IF STATMENT NUMBER 1
if(a>=18):
    print("You are eligible to vote.")
elif(a<0):
    print("Invalid age.")
elif(a==0):
    print("0 is not a valid age.")
else:
    print("You are not eligible to vote.")


#IF STATMENT NUMBER 2
if(a%2==0):
    print("Your age is even.")


#also if statement is independent and else and elif
#statement are depented on the if statment.
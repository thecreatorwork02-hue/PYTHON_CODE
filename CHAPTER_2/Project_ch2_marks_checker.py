Maths = float(input("Enter the marks of maths: "))
Physics = float(input("Enter the marks of physics: "))
Chemistry = float(input("Enter the marks of chemistry: "))  
total_marks = Maths + Physics + Chemistry
percentage = (total_marks/300)*100
print("the total marks is: " + str(percentage))

print("the score of 90% is achieved:" + str(percentage >= 90))
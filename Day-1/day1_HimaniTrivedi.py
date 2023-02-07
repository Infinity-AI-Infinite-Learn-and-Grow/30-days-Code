# Write a python code to take input from the user as username and country name. Also, Display both on screen.

print(input("Enter Username:"))
print(input("Enter country:"))

# Perform the below operation (At least two of them) on any two integer operands and then print the output on the screen:  
# *Addition(+), Subtraction (-), Multiplication(***), Modulus(%), Division(/), Exponential (***), Floor Division Operator(//)*.
a=int(input("A = "))
b=int(input("B = "))

print("Addition of", a ,"and",b,"is",a+b,sep=" ")
print("Subtraction of", a ,"and",b,"is",a-b,sep=" ")
print("Multiplication of", a ,"and",b,"is",a*b,sep=" ")
print("Modulus of", a ,"and",b,"is",a%b,sep=" ")
print("Division of", a ,"and",b,"is",a/b,sep=" ")
print("Exponential of", a ,"and",b,"is",a**b,sep=" ")
print("Floor Division of", a ,"and",b,"is",a//b,sep=" ")

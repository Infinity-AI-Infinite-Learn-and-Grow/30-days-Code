# Write a python code to take input from the user as username and country name. Also, Display both on screen. 

#Task1

username = input("Enter Your Name: ")
country_name = input("Enter Your Country Name: ")

print("Your Name is "+username+". You live in "+country_name+".")

#Task2

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Addition of {} and {} is: {}".format(num1, num2, num1+num2))
print("subtraction of {} and {} is: {}".format(num1, num2, num1-num2))
print("Multiplication of {} and {} is: {}".format(num1, num2, num1*num2))
print("Modulus of {} and {} is: {}".format(num1, num2, num1%num2))
print("Division of {} and {} is: {}".format(num1, num2, num1/num2))
print("{} to the power of {} is: {}".format(num1, num2, num1**num2))
print("Floor Division Operation between {} and {} is: {}".format(num1, num2, num1//num2))

# - Write a python code to take input from the user as username and country name.
# Also, Display both on screen.

username = input("Enter a username: ")
country = input("Enter the name of your country: ")
print("\nYour Details:")
print("---------------------------")
print("Username:\t", username)
print("Country:\t", country)
print("---------------------------\n")

# - Perform the below operation (At least two of them) on any two integer operands
# and then print the output on the screen: Addition(+) , Subtraction (-), Multiplication(),
# Modulus(%), Division(/), Exponential (*), floor division operator(//).

print("Enter two integer values")
n1 = int(input("Integer 1: "))
n2 = int(input("Integer 2: "))

print("\nArithmetic Operations:")
print("---------------------------")
print("{} + {} = {}".format(n1, n2, n1+n2))
print("{} - {} = {}".format(n1, n2, n1-n2))
print("{} * {} = {}".format(n1, n2, n1*n2))
print("{} % {} = {}".format(n1, n2, n1 % n2))
print("{} / {} = {}".format(n1, n2, round(n1/n2, 6)))
print("{} ** {} = {}".format(n1, n2, n1**n2))
print("{} // {} = {}".format(n1, n2, n1//n2))
print("---------------------------\n")

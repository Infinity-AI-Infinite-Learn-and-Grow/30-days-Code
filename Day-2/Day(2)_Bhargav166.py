# Declare a first name variable, last name variable, country variable,
# city variable, age variable, and Dob variable,
# Declare a variable is_true, You can Multiply the variable in one line.
# Check the data type of all your variables using the type() built-in function.

import datetime

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country's name: ")
city = input("Enter your city's name: ")
age = int(input("Enter your age: "))
DOB = input("Enter your Date of birth (in DD/MM/YYYY): ")
DOB = datetime.datetime.strptime(DOB, "%d/%m/%Y").date()

print("\nVariables\t\tType")
print("-----------------------------------------------")
print("First Name\t\t{}".format(type(first_name)))
print("Last Name\t\t{}".format(type(last_name)))
print("Country\t\t\t{}".format(type(country)))
print("City\t\t\t{}".format(type(city)))
print("Age\t\t\t{}".format(type(age)))
print("Date of Birth\t\t{}".format(type(DOB)))
print("-----------------------------------------------")

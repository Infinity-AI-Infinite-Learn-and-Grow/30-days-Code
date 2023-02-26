# 1. This is a Exception Handling Questions.
#  - names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
# Unpack the first five countries and store them in a variable nordic_countries,
# store Estonia and Russia in es, and ru respectively.

# 2. Input a name, Year you were born, and declare age variable.
# In age variable 2023 - year_born. Handle a type_error that occured.


# ---- Task 1 ----
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)

# ---- Task 2 ----

name = input("Enter your name: ")
year_born_input = input("Enter the year you were born: ")

try:
    year_born = int(year_born_input)
except TypeError:
    print("Error: Year of birth must be an integer.")
else:
    age = 2023 - year_born
    print("Hello, {}! You are {} years old.".format(name, age))

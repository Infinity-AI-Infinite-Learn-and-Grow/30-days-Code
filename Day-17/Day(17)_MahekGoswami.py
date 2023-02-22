#Day 17

#-------Task 1-------
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordic_countries=names
Finland, Sweden, Norway,Denmark,Iceland,es,ru = names

#-------Task 2-------
name = input("Enter your name: ")
year_born_input = input("Enter the year you were born: ")

try:
    year_born = int(year_born_input)
except TypeError:
    print("Error: Year of birth must be an integer.")
else:
    age = 2023 - year_born
    print("Hello, {}! You are {} years old.".format(name,age))
names = ['Finland', 'Sweden', 'Norway',
         'Denmark', 'Iceland', 'Estonia', 'Russia']
*nordic_countries, es, ru = names
print(nordic_countries)
print(es)
print(ru)


name = input("Enter your name: ")
born_year = input("Enter your birth year: ")
try:
    age = int(2023-born_year)
    print("You are {} years old.".format(age))
except TypeError:
    print("it's a type error")

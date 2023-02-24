names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru=names
print(nordic_countries)
print(es)
print(ru)


name=input("Enter your name: ")
born_year=input("Enter your birth year: ")
try:
    age=2023-born_year
except TypeError:
    print("it's a type error")






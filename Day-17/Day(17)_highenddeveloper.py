"""This is a Exception Handling Questions.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and
store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
Input a name, Year you were born, and declare age variable. In age variable 2023 - year_born. Handle a type_error that occured."""

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland','Estonia','Russia']
nordic_countries=names[0:5]
ru=names[-1]
es=names[-2]
print(nordic_countries)
print(ru)
print(es)

try:
    name=input("Enter your name:")
    year_born=int(input("Enter the year you were born:"))
    age=2023-year_born
    print(f"Hello {name} your age is {age}")
except TypeError:
    print("Type Error occured")


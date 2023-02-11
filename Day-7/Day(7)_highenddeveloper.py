it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = {22, 19, 24, 25, 26, 24, 25, 24}

"""Find the length of the set it_companies
Join A and B
Find A intersection B
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
"""

print(len(it_companies))

join=A.union(B)
print(join)

join1=A.intersection_update(B)
print(join)

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?

print(len(age))

print(len(ages))

if len(age) > len(ages):
    print("The length of List is greater than sets")
else:
    print("The length of Sets is greator than List")


#list is bigger
# - Sets:-
#     it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'},
#     A = {19, 22, 24, 20, 25, 26},
#     B = {19, 22, 20, 25, 26, 24, 28, 27},
#     age = [22, 19, 24, 25, 26, 24, 25, 24].

# - Find the length of the set it_companies
# - Join A and B
# - Find A intersection B
# - Convert the ages to a set and compare the length of the list and the set, which one is bigger?

from ntpath import join

# Find the length of the set it_companies
it_companies = {'Facebook', 'Google',
                'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'},
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Join A and B
print("The len of the it_companies is", len(it_companies))
print("Join A and B", A.union(B))

# Find A intersection B
print("The intersection B and A is", B.intersection(A))

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age1 = set(age)
print(age1)

print("Length of List is", len(age), "Length of sets is", len(age1))
if len(age) > len(age1):
    print("The length of List is greater than sets")
else:
    print("The length of Sets is greator than List")

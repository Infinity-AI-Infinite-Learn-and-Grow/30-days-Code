# - Sets:-
#     it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'},
#     A = {19, 22, 24, 20, 25, 26},
#     B = {19, 22, 20, 25, 26, 24, 28, 27},
#     age = [22, 19, 24, 25, 26, 24, 25, 24].

# - Find the length of the set it_companies
# - Join A and B
# - Find A intersection B
# - Convert the ages to a set and compare the length of the list and the set, which one is bigger?

it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age_list = [22, 19, 24, 25, 26, 24, 25, 24]

print("Length of Set it_companies:-", len(it_companies))

print("\nA:\t", A)
print("B:\t", B)
C = A.union(B)
print("A U B:\t", C)

C = A.intersection(B)
print("A ∩ B:\t", C)

age_set = set(age_list)
print("\nType\tSize")
print("----\t----")
print("List\t", len(age_list))
print("Set\t", len(age_set))
if (len(age_list) > len(age_set)):
    print("-> List is bigger than the set")
elif (len(age_list) > len(age_set)):
    print("-> Set is bigger than the list")
else:
    print("-> Both are of equal size")

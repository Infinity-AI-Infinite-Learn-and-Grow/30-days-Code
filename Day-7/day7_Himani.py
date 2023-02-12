
#- Find the length of the set it_companies



it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(len(it_companies))

#- Join A and B
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

joinAB=A.union(B)
print(joinAB)

#- Find A intersection B
print(A.intersection(B))

#- Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age = [22, 19, 24, 25, 26, 24, 25, 24]
ageSet=set(age)

if(len(age) > len(ageSet)):
    print("List Size is bigger by " , len(age)-len(ageSet))
else:
    print("Set Size is bigger by " , len(ageSet) - len(age))

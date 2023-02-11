# Day7
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Length of set it_companies
print("Length of it_companies set is : ",len(it_companies))

#Join A and B
set_join=A.union(B)
print("Join of A and B is : ",set_join)

#Intersection A and B
set_join=A.intersection(B)
print("Intersection of A and B is : ",set_join)

#List to set and comparing lenght
age_set=set(age)
print("Age in set form is : ",age_set)

if(len(age_set)>len(age)):
    print("Length of age set is bigger ")
elif(len(age_set)<len(age)):
    print("Length of age list is bigger ")
else:
    print("Both are of the same length")

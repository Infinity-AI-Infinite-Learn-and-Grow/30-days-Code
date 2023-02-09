IT_Company=["Google","Facebook","Tesla","Amazon","Microsoft"]
print(IT_Company[0],IT_Company[2],IT_Company[4])
#inserting  element to the list
IT_Company.insert(2,"walmart")
IT_Company.insert(5,"Apple")
print(IT_Company)
#reversing a list in descending order 
IT_Company.sort()
print(IT_Company)
IT_Company.reverse()
print(IT_Company)
#removing the last element from the list
a=len(IT_Company)
IT_Company.pop(a-1)
print(IT_Company)
#destroying the list
del IT_Company
print(IT_Company)




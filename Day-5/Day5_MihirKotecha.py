IT_Companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Amazon']

print("The first company in the list is: ", IT_Companies[0])
print("The middle company in the list is: ", IT_Companies[2])
print("The last company in the list is: ", IT_Companies[4])

IT_Companies.insert(1, 'IBM')
IT_Companies.insert(4, 'Oracle')

IT_Companies.sort()

IT_Companies.reverse()

print("The list in decreasing order: ", IT_Companies)

IT_Companies.remove(IT_Companies[len(IT_Companies)-1])

print("The list after removing the last company: ", IT_Companies)

IT_Companies.clear()

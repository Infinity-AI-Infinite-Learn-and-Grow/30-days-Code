#Day13

# ------Task 1------

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
new_numbers=[num for num in numbers if num<=0 ]
print(new_numbers)
print("\t")

# ------Task 2------
list_of_tuples=[(i, 1, i**1, i**2, i**3,i**4, i**5) for i in range(3)]
print(list_of_tuples)
# ------Task 3------

test_list=[[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dict_list=["country" , "city"]

list_of_dict = [{'country':i[0][0],'city':i[0][1]} for i in test_list]
print("Keys : " +str(list_of_dict))
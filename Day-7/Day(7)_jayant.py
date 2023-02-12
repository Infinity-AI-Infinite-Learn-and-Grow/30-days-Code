# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
a = {19, 22, 24, 20, 25, 26}
b = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]


l=len(it_companies)
print(l)

print(a-(a ^ b))



length=len(age)
set_age=set(age)
length1=len(set_age)
if(length1>=length):
    print("The length of set is equal to the length of list")
else:
    print("The length of set is smaller than the length of list")

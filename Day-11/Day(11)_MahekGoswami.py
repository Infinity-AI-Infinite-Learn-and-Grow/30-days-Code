#Day 11

# ------Task 1------
def add_two_numbers(x,y):
    return x+y

num1=int(input("Enter a number : "))
num2=int(input("Enter second number : "))
print("Sum of {} and {} is : {} ".format(num1,num2,add_two_numbers(num1,num2)))
print("\t")

# ------Task 2------
test_arr= [1, 2, 3, 4, 5]
def reverse_list(arr = []):
    for i in arr[::-1]:
        print(i)

print(reverse_list(test_arr))
print("\t")

# ------Task 3------
num=int(input("Enter a positive integer : "))
even_count, odd_count = 0, 0

for num in range(0,num+1):
    if num % 2 == 0:
        even_count += 1
 
    else:
        odd_count += 1
 
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
# 1. Declare a function add_two_numbers. It takes two parameters and returns a sum.
# 2. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# Output:
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
# 3. Declare a function named evens_and_odds. It takes a positive integer as a parameter and it counts a number of events and odds in the number.
# Output:
# print(evens_and_odds(100))
# # The number of odds is 50.
# # The number of events is 51.

# 1. Declare a function add_two_numbers. It takes two parameters and returns a sum.
def add_two_numbers(a, b):
    c = a+b
    return c


# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
a = 2
b = 2
sum = add_two_numbers(a, b)
print("Sum of {0} and {1} is {2}." .format(a, b, sum))
print("\n")


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array(use loops).

def reverse_list(arr=[]):
    for i in arr[::-1]:
        print(i, end="")
    print()


arr_num = [1, 2, 3, 4, 5]
arr_num1 = ["A", "B", "C"]
# print(arr_num)

a = reverse_list(arr_num)
b = reverse_list(arr_num1)


# 3. Declare a function named evens_and_odds.
# It takes a positive integer as a parameter and it counts a number of even and odds in the number.
# Output:
# print(evens_and_odds(100))
# # The number of odds is 50.
# # The number of events is 51.

def evens_and_odds(a):
    even = 1
    odd = 0
    for i in range(a):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return f"The number of odds are {odd}. The number of evens are {even}."


print(evens_and_odds(100))

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

from array import *


def add_two_numbers(n1, n2):
    return (n1+n2)


print("Summation of two numbers")
print("------------------------")
print("Enter any two numbers:")
n1 = float(input("Number 1: "))
n2 = float(input("Number 2: "))
sum = add_two_numbers(n1, n2)

print("Sum = {}".format(sum))
print()

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).


def reverse_list(arr):
    print("\nReversed array: ")
    for i in arr:
        print(arr[-i], end=" ")


arr = array('i', [1, 2, 3, 4, 5])
print("Original array: ")
for i in arr:
    print(arr[i-1], end=" ")
reverse_list(arr)
print("\n")


# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.

def evens_and_odds(n):
    odds = 0
    evens = 0
    for i in range(n+1):
        if (i % 2 == 0):
            evens += 1
        else:
            odds += 1
    return "The number of odds are {}\nThe number of evens are {}".format(odds, evens)


print("Odds and Evens")
print("--------------")
n = abs(int(input("Enter a positive number: ")))
print(evens_and_odds(n))

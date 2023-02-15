"""Declare a function add_two_numbers. It takes two parameters and it returns a sum. Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops). Output: print(reverse_list([1, 2, 3, 4, 5]))
[5, 4, 3, 2, 1]
print(reverse_list1(["A", "B", "C"]))
["C", "B", "A"]
Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number. Output: print(evens_and_odds(100)) # The number of odds are 50. # The number of evens are 51."""

def add_two_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def reverse_list(a):
    """Return the reverse of a list."""
    return a[::-1]

def reverse_list1(a):
    """Return the reverse of a list."""
    return a[::-1]
    
def evens_and_odds(a):
    """Return the number of evens and odds in a number."""
    evens=1
    odds=0
    for i in range(a):
        if int(i) % 2 == 0:
            evens=evens+1
        else:
            odds=odds+1
    return f"The number of odds are {odds}. The number of evens are {evens}."

print(add_two_numbers(1, 2))
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list1(["A", "B", "C"]))
print(evens_and_odds(100))

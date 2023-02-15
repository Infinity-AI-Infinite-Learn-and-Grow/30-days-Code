# 1. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print("#", end="")
        print()


# n = int(input("Enter number of rows: "))
pattern(7)

print("\n")

# 2. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100


def table(n):
    for i in range(1, n+1):
        print(i, "*", i, "=", i * i)


# n = int(input("Enter the table number: "))
table(10)

print("\n")

# 3. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# Output: The sum of all numbers is 5050.

count = 0
for i in range(0, 100+1):
    count = i + count
print(count)

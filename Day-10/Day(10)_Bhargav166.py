# 1. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

for i in range(7):
    for j in range(i+1):
        print("#", end="")
    print()
print()


# 2. Print the following pattern:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# ...

for i in range(11):
    print("{} x {} = {}".format(i, i, i*i))
print()

# 3. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# Output: The sum of all numbers is 5050.

sum = 0
for i in range(101):
    sum += i
print("Total sum:", sum)

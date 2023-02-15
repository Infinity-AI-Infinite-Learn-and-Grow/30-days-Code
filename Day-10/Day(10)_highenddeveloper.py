"""Day 10: In the GitHub repository, Infinity-AI(Infinite Learn and Grow)/30-days-code inside the Day-10 folder create your_name.py file as defined in the readme.md file.
1. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
  #
  ##
  ###
  ####
  #####
  ######
  #######
2. Print the following pattern:
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100
3. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
Output: The sum of all numbers is 5050."""

print("first loop")

for r in range(7):
  i="#"*r
  print(i)

print("second loop")

for i in range(11):
  j=i*i
  print(f"{i} x {i} = {j}")

print("third loop")

sum=0
for a in range(101):
  sum=sum+a
  
print(f"The sum of all number is {sum}")
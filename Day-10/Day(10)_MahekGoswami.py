#Day 10

# ------Task 1------
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        print("#",end='')
    print("\r")
print("\t")

# ------Task 2-------
for i in range(0, 11):
   print(i, 'x', i, '=', i*i)
print("\t")

# ------Task 10-------
sum=0
for i in range(0, 101):
   sum=sum+i
print("The sum of all numbers is : ",sum)
print('Print pattern 1')
for i in range(8):
    print('*'*i)
print('Print pattern 2')
for i in range(11):
    print("{} x {} = {}".format(i,i,i*i))

print('Print pattern 3')
sum=0
for i in range(101):
    sum+=i
print(sum)

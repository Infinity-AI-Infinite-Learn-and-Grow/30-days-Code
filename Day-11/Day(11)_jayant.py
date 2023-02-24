def add_two_numbers(a,b):
    return a+b
def reversed_list(l):
    s=[]
    for i in range(len(l)):
        s.append(l[len(l)-i-1])
    return s


d=[1, 2, 3, 4, 5]
e=["A", "B", "C"]
print(reversed_list(d))
print(reversed_list(e))

def even_and_odd(l):
    even=[]
    odd=[]
    for i in range(l):
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    if(l%2==0):
        even.append(l)
    else:
        odd.append(l)

    return (" number of even is: ",len(even)," number of odd is: ",len(odd))

print(even_and_odd(100))  
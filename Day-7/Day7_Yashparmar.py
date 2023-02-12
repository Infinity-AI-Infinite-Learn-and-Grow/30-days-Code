it_companies={'Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon'}

A={19,22,24,20,25,26}

B={19,22,20,25,26,24,28,27}

age=[22,19,24,25,26,24,25,24]

print("Length of It_companies is {}".format(len(it_companies)))

#join A and B

c=A.union(B)

print(c)

#instersection of A and B

a=A.intersection(B)

print(a)

#list to set converter

b=set(age)

print(b)

print("The length of the set is {}".format(len(age)))

print("The length of the list is {}".format(len(b)))

if len(age)>len(b) :

    print("The length of the set is bigger")

elif len(age)<len(b) :

     print("The length of the list is bigger")

else :

    print("Both have same length")

username = input("Enter your username: ")

country_name = input("Enter your country name: ")

print(username)
print(country_name)





cal=input("choose from list and type:\n-add\n-sub\nmultiply\ndivide\nmodulas\n")

a=int(input("enter the first number"))
b=int(input("entre the second number"))
add=lambda a,b: a+b #add
sub=lambda a,b: a-b  #sub
mul=lambda a,b: a*b  #mul
div=lambda a,b:a/b  #divude
mod=lambda a,b:a%b  #divide


if cal=="add":
    print(add(a,b))
    
elif cal=="sub":
    print(sub(a,b))
elif cal=="multiply":
    print(mul(a,b))
elif cal =="divide":
    print(div(a,b))
elif cal =="modulas":
    print(mod(a,b))
else:
    print("Enter the words again!")

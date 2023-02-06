add=lambda a,b: a+b #add
sub=lambda a,b: a-b  #sub
mul=lambda a,b: a*b  #mul
div=lambda a,b:a/b  #divude
mod=lambda a,b:a%b  #divide


cal=input("choose from list and type:\n-add\n-sub\nmultiply\ndivide\nmodulas\n")

a=input("enter the first number")
b=input("entre the second number")

if cal=="add":
    add(a,b)
elif cal=="sub":
    sub(a,b)
elif cal=="multiply":
    mul(a,b)
elif cal =="divide":
    div(a,b)
elif cal =="modulas":
    mod(a,b)
else:
    print("Enter the words again!")

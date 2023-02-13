#Day 9

#------Task1------
age=int(input("Enter your age : "))

if(age>=18):
    print("You are old enough to learn to drive!")
else:
    print("You need {} more years to learn to drive".format(18-age))
print("\t")

#------Task2------

my_age=20
print("My age is : ",my_age)
your_age=int(input("Enter your age : "))

if my_age > your_age:
    if my_age - your_age == 1:
        print("I am one year older than you.")
    else:
        print("I am {} years older than you.".format(my_age - your_age))
else:
    print("You are {} years older than me.".format(your_age - my_age))
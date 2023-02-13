a=int(input("Enter your age :- "))

if a>=18 :

    print("You are old enough to drive")

else :

    print("You need {} more years to learn to drive".format(18-a))

    

my_age=19

your_age=int(input("Enter your age:- "))

if abs(my_age-your_age)==1:

    print("There is a one year difference")

elif my_age==your_age:

    print("Both of us have same age")

elif  my_age>ypur_age:

    print("You are {} younger then me ".format(my_age-your_age))

else  :

    print("You are {} older then me ".format(abs(my_age-your_age)))

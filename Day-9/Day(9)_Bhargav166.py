# 1. Get user input using input(“Enter your age: ”). If user is 18 or older,
# give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.

age = int(input("Please enter your age: "))
if age >= 18:
    print("You are old enough to drive")
else:
    print("You need to wait {} years before proceeding any further".format(18-age))
print()

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)?
# Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
# Output:
# Enter your age: 30
# You are 5 years older than me.

# Let's assume
your_age = int(input("Your age is: "))
my_age = int(input("My age is: "))

if your_age > my_age:
    if (your_age - my_age) == 1:
        print("You are 1 year older than me")
    else:
        print("You are {} years older than me".format(your_age - my_age))
elif my_age > your_age:
    if (my_age - your_age) == 1:
        print("I am 1 year older than you")
    else:
        print("I am {} years older than you".format(my_age - your_age))
else:
    print("We are of same age")

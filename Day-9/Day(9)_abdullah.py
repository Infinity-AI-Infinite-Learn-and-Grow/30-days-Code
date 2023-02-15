# Day 9: In the GitHub repository, Infinity-AI(Infinite Learn and Grow)/30-days-code inside
# the Day-9 folder create your_name.py file as defined in the readme.md file.

# Get user input using input(“Enter your age: ”).
# If user is 18 or older, give feedback: You are old enough to drive.
# If below 18 give feedback to wait for the missing amount of years.
# Output: Enter your age: 30 You are old enough to learn to drive.
# Output: Enter your age: 15 You need 3 more years to learn to drive.

# Compare the values of my_age and your_age using
# if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for
# bigger differences, and a custom text if my_age = your_age.
# Output: Enter your age: 30 You are 5 years older than me.


age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to learn to drive")
else:
    print("You need", 18-age, "more years to learn to drive")


my_age = 19
your_age = int(input("Enter your age: "))
if your_age > my_age:
    print("You are ", your_age-my_age, " years older than me")
elif your_age < my_age:
    print("You are ", my_age-your_age, " years younger than me")
else:
    print("We are of same age")

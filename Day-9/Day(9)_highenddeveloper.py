#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output: Enter your age: 30 You are old enough to learn to drive. Output: Enter your age: 15 You need 3 more years to learn to drive.
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output: Enter your age: 30 You are 5 years older than me.

user=int(input("Enter the user age: "))

year=18-user
if user>=18:
  print("You are old enough to drive.")

else:
  print(f"You need {year} year to learn to drive")

#age check
my_age=int(input("Enter your age: "))
age=21

a=age-my_age
b=my_age-age
if my_age>age:
  print(f"You are {b} years younger than me")

elif my_age<age:
  print(f"You are {a} years older than me")
else:
  print("Your age is equal")
  





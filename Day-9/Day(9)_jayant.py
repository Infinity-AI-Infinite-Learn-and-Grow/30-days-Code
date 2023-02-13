age=int(input("Enter your age: "))
if age>=18:
    print("You are old enough to drive")
else:
    print("wait for ",18-age," years")


my_age=19
your_age=int(input("Enter your age: "))
if your_age>my_age:
    print("You are ",your_age-my_age," years older than me")
elif your_age<my_age:
    print("You are ",my_age-your_age," years younger than me")
else:
    print("We are of same age")
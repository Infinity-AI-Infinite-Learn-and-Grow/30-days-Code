##- Write a script that prompts the user to enter the base and height of the triangle and calculate the area of this triangle (area = 0.5 x b x h).
##- Get the radius of a circle using the prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.


#area of trainge
b=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of triange:"))
area=0.5*b*h
print("area of triange is:" + str(area))

#area of circle and circumference
r=int(input("Enter the radius of circle:"))
pi=3.14
areac=pi*r*2
print("area of circle is:"+ str(round(areac,2)))
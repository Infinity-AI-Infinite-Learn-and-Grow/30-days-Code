# Write a script that prompts the user to enter the base and height of the triangle and calculate the area of this triangle (area = 0.5 x b x h).
#

base=float(input("Enter Base :"))
height=float(input("Enter height :"))

print("Area : ",format(0.5*base*height,'.2f'))

# Get the radius of a circle using the prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius=float(input("Enter radius :"))

print("Area : ",format(3.14*pow(radius,2),'.2f'))
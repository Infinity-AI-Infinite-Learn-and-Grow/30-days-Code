#  Write a script that prompts the user to enter the base and height of the triangle
# and calculate the area of this triangle (area = 0.5 x b x h).
# Get the radius of a circle using the prompt.
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

base = int(input("Enter the base of the triangle: "))
height = int(input("Enter the height of the triangle: "))
area = 0.5 * float(base) * float(height)
print("Enter the area of the triangle is: ", area)

radius = input("Enter the radius of the circle: ")
area = 3.14 * float(radius) * float(radius)
print("The area of the circle is: ", area)

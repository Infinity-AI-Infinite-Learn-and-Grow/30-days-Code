# - Write a script that prompts the user to enter the base and
# height of the triangle and calculate the area of this triangle (area = 0.5 x b x h).
# - Get the radius of a circle using the prompt.
# Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

print("To find area of a triangle")
print("--------------------------")
base = input("Enter the base of the triangle: ")
height = input("Enter the height of the triangle: ")
area = 0.5 * float(base) * float(height)
print("-> Area of the triangle: {}".format(area))

print("\nTo find area and circumference of a circle")
print("------------------------------------------")
radius = input("Enter the radius of the circle: ")
pi = 3.14
area = pi * float(radius) * float(radius)
circumference = 2 * pi * float(radius)
print("-> Area of the circle: {}".format(area))
print("-> Circumference of the circle: {}".format(circumference))

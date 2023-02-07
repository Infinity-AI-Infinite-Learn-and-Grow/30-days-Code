#Variables

T_base = float(input("Enter the Base of the Triangle: "))
T_height = float(input("Enter the Height of the Triangle: "))
C_rad = float(input("Enter Radius of a Circle: "))
pi = 3.14

#Calculation

print("Area of the Triange is {}".format(0.5*T_base*T_height))
print("Area of the Circle is {}".format(pi*(C_rad**2)))
print("Circumference of the Circle is {}".format(2*pi*C_rad))

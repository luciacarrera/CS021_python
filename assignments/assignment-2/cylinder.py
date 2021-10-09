# Lucía Carrera
# CS21
# Calculate surface area and volume of user's cylinder



## Constants
PI = 3.14159265359

## Ask user to input the dimensions of the cylinder
# radius of base
radius_base = float(input("What is the radius of the base of the cylinder? "))

# height
height = float(input("What is the height of the cylinder? "))



## Calculate surface area and volume of cylinder with above dimensions
# surface area
surface_area = 2*PI*radius_base*height + 2*PI*radius_base**2

# volume
volume = PI*radius_base**2*height



## Print results of the calculations
# surface 
print("The surface area of the cylinder is: {:.2f}".format(surface_area))

# volume
print("The volume of the cylinder is: {:.2f}".format(volume))


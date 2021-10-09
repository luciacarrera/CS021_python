# Lucía Carrera
# CS021 A
# Program that ask converts a mass inputed by a user into weight

# Constant to represent gravity
GRAVITY = 9.8

# Ask for mass
mass = float(input("Enter the object's mass in kilograms: "))

# Check if input incorrect
if mass < 0:
    print("Mass must be >= 0")

# If correct continue  
else:

    # Calculate weight (Newton formula)
    weight = mass * GRAVITY

    # Print result
    print(f"Object Weight: {weight:.2f} newtons")


    # Display if weight is heavy or light (if normal do not display anything)
    if weight > 500:
        print("The object is too heavy. It weighs more than 500 newtons.")

    # use of elif so program doesnt unneccessarily run code
    elif weight < 100:
        print("The object is too light. It weighs less than 100 newtons.")

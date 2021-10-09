# Lucía Carrera
# CS021 A
# Program that calculates number of cartons needed for the eggs collected

# Constant
DOZEN = 12

# descriptive print (could be part of input but less readable)
print("This program will determine the required number of 1-dozen egg cartons.")

# ask user for eggs collected
EGGS = int(input("How many eggs did you collect today? "))

# check input
if EGGS <0:
    print("Your value cannot be negative.")
    
else:

    # calculate number of cartons assuming remainder is 0
    cartons = int(EGGS / DOZEN)

    # check left over eggs
    leftovers = EGGS % DOZEN
    
    # print result
    print(f"We will pack your {EGGS} eggs in {cartons} cartons.")
    print(f"There will be {leftovers} eggs left over.")

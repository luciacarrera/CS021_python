# Lucía Carrera
# CS 021 A
# Program used to create a multiplication table according to user input

## INPUT
# get user to input a starting number for the range
start = int(input("Enter a positive starting value < 1000: "))

# if invalid input ask user again until start is correct
while (start <= 0 or start >= 1000):
    start= int(input(f"{start} is not a valid choice, try again\nEnter a positive starting value < 1000: "))

# get user to input an ending number for the range
end = int(input("Enter a positive ending value less than 1000 and greater than the starting value: "))

# if invalid input ask user again until end is correct
while (end <= 0 or end >= 1000 or end <= start):
    end= int(input(f"{end} is not a valid choice, try again\nEnter a positive starting value < 1000: "))

# newlines printed for readability
print("\n\n")

# CALCULATIONS
for row in range(start-1,end+1,1):

    # resetting of string variable
    myStr= ""

    # if statement to print an empty space in the first row of table
    if (start-1 == row):
        myStr = f"\t"

    # rest of the rows in table
    else:
        myStr = f"{row:8d}"

    # for loop to include the numbers of each row
    for col in range(start,end+1,1):

        # first row of table is just multiplied by 1
        if(start-1 == row):
            myStr += f"{col*1:8d}"
        # rest is multiplied by row and column
        else:
            myStr += f"{col*row:8d}"

    # prints row
    print(myStr)

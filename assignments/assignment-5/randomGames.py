# Lucía Carrera
# CS 021 A
# Program that allows user to play several games that involve randomness.

# IMPORT STATEMENTS
import random

# global constants
MIN_DICE = 1
MIN_SIDES = 1

##  MAIN FUNCTION
def main():
    
    # constants
    OPT_DICE = 1
    OPT_BINGO = 2
    OPT_QUIT = 3
    

    # user will first read the menu options and pick an option
    menu()
    choice = int(input("What option do you choose? "))

    # input validation, if quit option program will end
    while choice != OPT_QUIT:
        
        # if choice is dice
        if choice == OPT_DICE:

            # ask user for number of dice
            num_die = int(input("How many dice do you want to roll? "))

            # input validation of number of dice
            while num_die < MIN_DICE:
                print("Number of dice must be greater than 0! ")
                num_die = int(input("How many dice do you want to roll? "))

            # ask user for number of sides on dice
            sides = int(input("How many sides are on each die? "))

            # input validation of sides on dice
            while sides < MIN_SIDES:
                print("Number of sides must be greater than 0! ")
                sides = int(input("How many sides are on each die? "))
            
            dice(num_die, sides)

        # if choice is bingo
        elif choice == OPT_BINGO:
            bingo()
            
        # tells user that they picked the wrong option
        else:
            print("Please pick an option from the menu! ")
            
        # goes to menu function
        menu()
                        
        # asks user in what option they are interested in 
        choice = int(input("What option do you choose? "))

    # end of while loop
        
# end of main function


     
## MENU FUNCTION
# A function that prints the menu of options for the screen 
def menu():

    # prints menu option
    print("Use the numbers to select an option: \n1: Roll some dice! \n2: Play Some Bingo! \n3: Quit ")


## DICE FUNCTION
# A function that simulates the rolling of dice
def dice(num, sides):

    # variable to sum each roll
    total = 0
    
    # for loop to print each individual roll
    for i in range(MIN_DICE,num+1):

        # selects random number according to number of sides in dice
        result = random.randint(MIN_SIDES, sides+1)

        # prints result
        print(f"Roll number {i} is {result}")

        # sums this roll
        total += result

    # prints sum of rolls
    print(f"Total of all rolls is: {total}")

    
## BINGO FUNCTION
# function that simulates a random Bingo draw
def bingo():
    # letter cutoffs
    MIN = 1
    B_CUTOFF = 15
    I_CUTOFF = 30
    N_CUTOFF = 45
    G_CUTOFF = 60
    MAX = 75
    
    # random number generator
    num = random.randint(MIN,MAX)
    letter = ""

    # Divides search into two:
    # Searches only for BIN
    if num < N_CUTOFF: 
        if num < B_CUTOFF:
            letter = "B"
        elif num < I_CUTOFF:
            letter = "I"
        else:
            letter = "N"
    # Searches only GO
    else: 
        if num < G_CUTOFF:
            letter = "G"
        else:
            letter = "O"

    # Prints statement with corresponding letter and number 
    print(f"The next number in Bingo is: {letter}{num}")
    
main()

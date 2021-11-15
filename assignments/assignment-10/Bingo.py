# Lucía Carrera
# CS 021 A
# Program that draws bingo draws, tracking that no two same bingo draws are drawn.

# import statement
import random

def main():

    # initializing default response
    response = 'n'

    # initializing set to keep track of bingo draws
    draws = set()
    
    # while loop until user reports that someone has won
    while response != 'y':

        # vars initialized for following while loop to work appropriately
        myboolean = False
        draw = ""

        # while loop to call bingo() function until bingo drawn has not yet been called
        while myboolean == False:
            draw = bingo()

            # check if already drawn
            if draw not in draws:
                draws.add(draw)
                myboolean = True

        # print unrepeated bingo draw
        print(f"The current draw is: {draw}")
        
        # ask user if someone has won
        response = input("Did anyone win the game? Y/N ").lower()

        # if they didnt reply y or n be annoying until they do
        while response != 'y' and response != 'n':
            print("Please respond with just the letters Y or N ")
            response = input("Did anyone win the game? Y/N ").lower()

    # ask user if they want to play again
    response = input("Would you like to play again? Y/N ").lower()
    
    # if they didnt reply y or n be annoying until they do
    while response != 'y' and response != 'n':
        print("Please respond with just the letters Y or N ")
        response = input("Would you like to play again? Y/N ").lower()

    # if response is y restart game
    if response == 'y':
        main()




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

    # create string to return
    return f"{letter}{num}"


main()

# Lucía Carrera
# CS 021 A
# Program that plays the game of 21 with the user.

# IMPORT statement
import random

def main():

    # constants
    MAX_USER_POINTS = 21


    # initializing user's and computer's totals and play
    user_total = 0
    computer_total = 0
    play= "y"
    
    # while loop that will keep game going until user decides not to play anymore
    while(play == "y" and user_total < MAX_USER_POINTS):
        # asking user if they want to play again
        play = get_response()
        
        # rolling dice
        user_roll, computer_roll = roll_dice()

        # adds roll to total points for computer and user
        user_total += user_roll
        computer_total += computer_roll

        #print result of user's total points
        print(f"Points: {user_total}")
        
        
    # end of first while loop
    # print statement saying points of user and computer
    print(f"User's points: {user_total}\nComputer's points: {computer_total}")

    # if statement to determine the winner of the game
    if(user_total > computer_total or user_total >= 21):
        print("User wins")
    elif(user_total < computer_total):
        print("Computer wins")
    else:
        print("Tie Game!")



# function that simulates the rolling of two dice
def roll_dice():

    # random number between 1 and 6 (inclusive) drawn for both players
    user_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    # returns rolls
    return user_roll, computer_roll



# function that asks user if they want to keep playing
def get_response():

    # asks user if they want to play
    response = input("Do you want to roll? ")

    # checks if user doesnt know how to understand instructions
    while(response != "n" and response!="y"):
        response = input("Please respond with y or n: ")

    return response

main()

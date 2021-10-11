# Lucía Carrera
# CS 021 A
# Program to compute the total cost of gasoline used during your most recent trip.

def main():
    
    # initial print statement
    print("\nComputing your gasoline expenses...")

    response = "y"
    
    # while loop to make main run until user wants to quit
    while (response != "n"):
        
        # prompt user for total miles driven
        miles_driven = float(input("\nTotal miles: "))

        # input validation
        while(miles_driven < 0):
            miles_driven = float(input("Enter a value > 0: "))
            
        # prompt user for % in highway
        percent_highway = float(input("Percentage of total miles driven on a highway: "))

        # input validation
        while(percent_highway < 0 or percent_highway >100):
            percent_highway = float(input("Enter a value > 0 and < 100: "))

        gallons = total_gallons(miles_driven, percent_highway)
        cost = gas_expense(gallons)

        print(f"\nTotal miles: {miles_driven:.1f}\nGas consumption: {gallons:.1f} gal\nTotal cost: $ {cost:.2f}\n")

        # ask user if they want to calculate another trip cost
        response = input("Compute gas expense for another trip (y or n)? ")

        #input validation so that if response is not y or not n it will not exit,
        while (response != "y" and response != "n"):
            response = input("Please respond with a y or n: ")

    
# function computes the total gas consumption (gallons)
def total_gallons(miles, percentage):
    
    # constant values of mpg for 2021 mini cooper
    MPG_HWY = 38
    MPG_CITY = 28

    # calculation of miles hwy and in city
    miles_hwy = miles * (percentage / 100)
    miles_city = miles - miles_hwy

    # formula for total gas consumption
    total_gas_consumption = (miles_hwy / MPG_HWY ) + ( miles_city/ MPG_CITY)

    return total_gas_consumption



# function that computes the total spent on gasoline for this trip.
def gas_expense(gallons):
    # constant value of price of gasoline per gallon
    COST_PER_GALLON = 2.29

    # calculates total spent on gas
    cost = COST_PER_GALLON * gallons
    return cost

main()

# Lucía Carrera
# CS 021 A
# Program to display users' amortization table

## CONSTANTS
# months in a year
MONTHS_IN_YEAR = 12



## INPUT
principal = float(input("Original loan amount? "))
apr = float(input("Annual interest rate? "))
years = int(input("Years? "))



## INITIAL CALCULATIONS
# n = amount of payments that will be made to pay off loan
n = years * MONTHS_IN_YEAR
monthly_rate = apr / MONTHS_IN_YEAR / 100
monthly_payments = round((monthly_rate * principal) /(1 -1 * ( 1 + monthly_rate ) ** -n) , 2 )

# Print monthly payment amount
print(f"Payment is $ {monthly_payments:.2f}")

# Print headers
print("Month   Interest  Cumulative    Principal     ")
print("       this month  Interest ")
        
# cumulative interest
cumulative = 0



## FURTHER CALCULATIONS + PRINTING RESULTS
# for loop to print out what the user will be paying each month
for month in range(1,n+1):

        # further calculations based on formulas found in assignment
        interest = principal * monthly_rate
        cumulative = cumulative + interest
        principal = principal - ( monthly_payments - interest )

        # print results with proper formatting
        print(f"{month:4}{interest:11.2f}{cumulative:11.2f}{principal:15.2f}")

        


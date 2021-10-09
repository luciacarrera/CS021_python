# Lucía Carrera
# CS21
# Calculate monthly payment,total amount paid and total interest paid of user's loan



## Constants
# months in a year
MONTHS_IN_YEAR = 12



## Ask user to input information about their loan
# amount of money to loan (principal)
principal = int(input("How much would you like to borrow? "))

# interest rate annual percentage rate (in percentage format %)
apr = float(input("What is the interest rate (APR) of the loan? "))

# years to pay off loan
years = float(input("How many years will it take to pay off the loan? "))



## Calculations
# amount of payments that will be made to pay off loan (n)
n = years * MONTHS_IN_YEAR

# monthly rate (from percentage to decimal format)
monthly_rate = apr /(MONTHS_IN_YEAR * 100)

# monthly payments
monthly_payments = (monthly_rate * principal) /(1 -1*(1+monthly_rate)**-n)

# total amount paid
total_paid = monthly_payments * n

# total interest paid
total_interest = (monthly_payments * years * MONTHS_IN_YEAR) - principal



## Print results
# monthly payments
print("The monthly payments are ${:.2f}".format(monthly_payments))

# amount paid
print("The total amount paid is ${:.2f}".format(total_paid))

# total interest paid   
print("The total interest paid to the bank is ${:.2f}".format(total_interest))

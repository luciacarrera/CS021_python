
MIN = 1
MAX = 99
QUARTER = 25
DIME = 10
NICKEL = 5
PENNY = 1

def main():
    change = int(input("How much change do you need in cents? "))
    while change > MAX or change < MIN :
        change = int(input(f"The change must be betweeen {MIN} cent and {MAX} cents!\nHow much change do you need in cents? "))
    change_calculator(change)
        
def change_calculator(change):
    # quarters 25
    # dimes 10
    # nickels 5
    # pennies 1
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if( change > QUARTER):
        quarters = change // QUARTER
        change = change % QUARTER

    if change > DIME :
        dimes = change // DIME
        change = change % DIME

    if change > NICKEL :
        nickels = change // NICKEL
        change = change % NICKEL

    if change > PENNY :
        pennies = change // PENNY
        change = change % PENNY

    print(f"{quarters} Quarters\n{dimes} Dimes\n{nickels} Nickels\n{pennies} Pennies")

main()

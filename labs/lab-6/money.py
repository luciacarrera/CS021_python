def main():
    dollars = float(input("Let's convert your US Dollars to Canadian Dollars \nEnter the value of your US Dollars: "))
    can = usd2can(dollars)
    print(f"This amount is worth $ {can:.2f} Canadian dollars")
    

def usd2can(dollars):
    RATE = 1.33
    canadian_dollars = RATE * dollars
    return canadian_dollars
main()

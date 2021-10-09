
print("Welcome to my leap year calculator.\nIf you give me a year, I can tell you if it is a leap year or not.")
year = int(input("What year? "))

if year < 0:
    print("Error: year not valid")
else:
    if year % 4 != 0:
        leap_year = "NOT"
    elif year % 100 != 0:
        leap_year = "IS"
    elif year % 400 != 0:
        leap_year = "NOT"
    else:
        leap_year = "IS"

    print("The year",leap_year,"a leap year.")

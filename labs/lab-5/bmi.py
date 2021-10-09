
def main():
    MIN_WEIGHT = 75
    MAX_WEIGHT = 350

    MIN_HEIGHT = 50
    MAX_HEIGHT = 350

    weight = float(input("Enter weight: "))
    while weight > MAX_WEIGHT or weight < MIN_WEIGHT :
        print("Invalid weight try again!")
        weight = float(input("Enter weight: "))


    height = float(input("Enter height: "))

    while height > MAX_HEIGHT or height < MIN_HEIGHT :
        print("Invalid height try again!")
        height = float(input("Enter height: "))

    display_BMI(weight, height)
    
def display_BMI(weight, height):
    UNDERWEIGHT_LIM = 18.5 # upper limits
    NORMAL_LIM = 24.9
    OVERWEIGHT_LIM = 29.9 # above is obese
    
    bmi = weight * 703/(height ** 2)
    status = ""
    
    if bmi < UNDERWEIGHT_LIM :
        status = "underweight"

    elif bmi > UNDERWEIGHT_LIM and bmi < NORMAL_LIM:
        status = "normal"

    elif bmi < OVERWEIGHT_LIM and bmi > NORMAL_LIM:
        status = "overweight"
    else:
        status = "obese"

    print(f"BMI = {bmi:.1f} {status}")
main()

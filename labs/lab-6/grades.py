def main():
    s1 = int(input("Enter score 1: "))
    s2 = int(input("Enter score 2: "))
    s3 = int(input("Enter score 3: "))
    s4 = int(input("Enter score 4: "))
    s5 = int(input("Enter score 5: "))

    print("Scores\tnumeric grade\tletter grade")
    print("------------------------------------------------")
    l1 = determine_grade(s1)
    l2 = determine_grade(s2)
    l3 = determine_grade(s3)
    l4 = determine_grade(s4)
    l5 = determine_grade(s5)

    print(f"score 1:\t{s1}\t{l1}")
    print(f"score 2:\t{s2}\t{l2}")
    print(f"score 3:\t{s3}\t{l3}")
    print(f"score 4:\t{s4}\t{l4}")
    print(f"score 5:\t{s5}\t{l5}")
    print("------------------------------------------------")
    av = calc_average(s1, s2, s3, s4, s5)
    print(f"Average score: {av}\t{determine_grade(av)}")

          
def calc_average(test1, test2, test3, test4, test5):
    ARG = 5
    av = (test1 + test2 + test3 + test4 + test5)/ARG
    return av

def determine_grade(score):
    letter = ""
    if score < 60:
        letter = "F"
    elif score <70:
        letter = "D"
    elif score <80:
        letter = "C"
    elif score <90:
        letter = "B"
    else:
        letter = "A"
    return letter


main()

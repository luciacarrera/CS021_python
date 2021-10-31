# Lucía Carrera
# CS 021 A
# Program to collect user input, compute total pay,
#and write user and summary information to a text file. 

def main():

    # STEP 1: POPULATE THREE LISTS
    # declarations of list
    names = []
    hours = []
    rates = []

    # while loop to get info from user
    name = input("Name (just hit Enter when done): ")
    while name != '':


        # exceptions to check if correct amount placed and if not restart
        try:
            hour = float(input("Hours worked: "))
        except:
            print("Values must be numeric.\nPlease input employee's name and values again.")
        else:
            
            # nested exception to restart if wrong
            try:
                rate = float(input("Hourly rate: "))
            except:
                print("Values must be numeric.\nPlease input employee's name and values again.")

            # if all correct then add to list
            else:
                names.append(name)
                hours.append(hour)
                rates.append(rate)
                
        # restart loop, if empty then it will stop
        name = input("Name (just hit Enter when done): ")



    # STEP 2: CREATE PAYROLL.TXT
    # try-catch in case file doesnt create correctly
    try:
        outfile = open('payroll.txt','w')
    except:
        print("Error: could not create payroll.txt")
    else:

        # initialization of variables & constants to print total and average
        PEOPLE = len(names)
        total = 0
        mystr = "" # string to hold info to print

        # for loop to go through each person
        for i in range(0,PEOPLE):
            
            # calculate individual person's pay
            pay = hours[i] * rates[i]
            
            # string to print in outfile
            mystr = f"{names[i]}\t\t{hours[i]:.2f}\t{rates[i]:.2f}\t{pay:.2f}\n"

            # adding person's pay to total
            total += pay

            # print in outfile
            outfile.write(mystr)
            
        # end of for loop
        
        # calculating average
        avg = total / PEOPLE

        # printing total payroll and average
        mystr = f"\nTotal Payroll = ${total:.2f}\nAverage Paycheck = ${avg:.2f}"
        outfile.write(mystr)

        # close file
        outfile.close()
        
    # end of else
# end of main()


main()

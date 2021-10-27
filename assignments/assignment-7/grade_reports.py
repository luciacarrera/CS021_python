# Lucía Carrera
# CS 021 A
# Program that produces a list of the grades of the students in a class
# and a report of with statistics and a histogram of the class

def main():
    
    ## CONSTANTS
    ASSIGNMENTS = 6

    ## GET FILE WITH GRADES
    # get file name with function
    file1 = get_file_name("grade input")
    try:
        infile=open(file1,'r')
        
    # error handling of file 1
    except:
        print("Could not open input file. Exiting now ")

    # if no errors opening file 1
    else:

        ## OPEN OUTPUT FILE 1
        # get file name with function
        file2 = get_file_name("outputting individual student grades")

        # error handling
        try:
            indiv = open(file2,'w')

        except: 
            print("Could not open output file.")

        # if opens correctly then write info
        else:
            # initialization of variables we will use for our stats
            high = 0
            low = 100
            count_a, count_b, count_c, count_d, count_f = 0,0,0,0,0
            numstds = 0
            sumgrades = 0

            # first name in sheet
            name = infile.readline().rstrip()

            # loops until end of page
            while name != '':

                # initialization of vars to use in for loop
                stpts = 0
                pts = 0

                # gets assignments grades
                for i in range(0,ASSIGNMENTS):
                    stpts += int(infile.readline().rstrip())
                    pts += int(infile.readline().rstrip())

                ## OPERATIONS FOR FIRST OUTPUT FILE 
                # calculate average of student
                grade = stpts / pts * 100

                # gets letter grade
                letter = determine_grade(grade)

                # writes in output file 1
                strIndiv = name+" "+letter+"\n"
                indiv.write(strIndiv)
                

                ## STATISTICS FOR SECOND OUTPUT FILE
                # see if higher or lower than vars
                if grade > high:
                    high = grade                
                if grade < low :
                    low = grade

                # count number of letters
                if letter == "A":
                    count_a +=1
                elif letter == "B":
                    count_b +=1
                elif letter == "C":
                    count_c +=1
                elif letter == "D":
                    count_d +=1
                else:
                    count_f +=1
                    
                # average calculations
                numstds +=1
                sumgrades += grade
                
                # gets next name
                name = infile.readline().rstrip()
                
            # end of while loop
            ## OPEN FOR SECOND OUTPUT FILE
            # get file name
            file3 = get_file_name("Grade report")
            
            # error handling
            try:    
                report = open(file3,'w')
            except: 
                print("Could not open output file.")
            else:
                ## CALCULATIONS FOR SECOND OUTPUT FILE
                # average
                avg = sumgrades / numstds
                # first three lines
                strreport = f"Highest grade: {high:.1f}\nLowest grade: {low:.1f}\nAverage grade: {avg:.1f}\n\n"
                report.write(strreport)
                report.close()

                # create histogram
                histogram("A", count_a, file3)
                histogram("B", count_b, file3)
                histogram("C", count_c, file3)
                histogram("D", count_d, file3)
                histogram("F", count_f, file3)
                




# function that gets the file name from user
def get_file_name(searchFile):
    userFile = input(f"What is the name of the file to use for {searchFile}? ")
    return userFile

# function that get the letter equivalent from grade
def determine_grade(grade):
    letter= ""
    if(grade>90):
        letter = "A"
    elif(grade>80):
        letter = "B"
    elif(grade>70):
        letter = "C"
    elif(grade>60):
        letter = "D"
    else:
        letter = "F"
        
    return letter


# function that makes a histogram
def histogram(label, count, outfile):
    try: # error
        file = open(outfile, 'a')
    except:
        print("Could not open file")
    else:
        line = label + ": "
        for i in range(0, count):
            line += "*"
        line +="\n"
        file.write(line)
        file.close()
        
main()     

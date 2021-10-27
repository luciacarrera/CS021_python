# Lucía Carrera
# CS 021 A
# Program that ...

def main():
    
    ## CONSTANTS
    ASSIGNMENTS = 6

    ## GET FILE WITH GRADES
    file1 = get_file_name("grade input")
    try:
        infile=open(file1,'r')
        
    # error handling of file 1
    except:
        print("Could not open input file. Exiting now ")

    # if no errors opening file 1
    else:

        # processing of information from input file
        aline = infile.readlines()

        # variables to keep track of information
        indiv_str, name = ("",)*2
        student_points, total_points, students, high, i = (0,)*5
        count_a, count_b, count_c, count_d, count_f = (0,)*5
        low = 100
            
        for line in aline:
            # removes unwanted newlines from line
            line = line.rstrip()
                
            ## READING STUDENT NAME
            if i == 0:
                # check that not a number grade
                if line.isnumeric() != True:
                    name = line
                else:
                    print(line)
                    print("Invalid student name")

            ## READING NUMBERS
            else:
                # error handling by making sure it is an integer
                try:
                    num = int(line)
                except:
                    print("Invalid grade")
                else:

                    # reading students grade
                    if i % 2 != 0:
                        student_points += num
                        
                    # reading total points available
                    else:
                        total_points += num

                        # if line in last assignment than we do extra calculations for our output files
                        if i == ASSIGNMENTS * 2:

                            ### INDIVIDUAL STUDENTS GRADES
                            grade = student_points / total_points *100
                            letter = determine_grade(grade)

                             # add to letter counter
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

                            # adds line to what we are going to print out
                            # could use append but I think this way makes more sense due to samples
                            indiv_str += name + " " + letter + "\n" # will add a newline to end
                                
                            # get statistics
                            if student_points > high:
                                high = student_points
                                    
                            if student_points < low :
                                low = student_points

                                
                            # resetting variables and summing total variables
                            students += 1
                            student_points = 0
                            total_points = 0
                            i = -1

            # end of else in for loop             
            i += 1
            
        # end of for loop

        
        ## GET OUTPUT FILE 1        
        # get 1st output file, if cannot be opened, program can still continue
        file2 = get_file_name("outputting individual student grades")
        try:
            indiv = open(file2,'w')

        # error handling of file 2
        except: 
            print("Could not open output file.")
            errFile2 = True
        else:
            indiv.write(indiv_str)
            indiv.close()
            
        ## GET OUTPUT FILE 2
        file3 = get_file_name("Grade report")
        try:    
            report = open(file3,'w')
            
        # error handling of file 3
        except: 
            print("Could not open output file.")
        infile.close()
        indiv.close()
        report.close()
        
def get_file_name(searchFile):
    userFile = input(f"What is the name of the file to use for {searchFile}? ")
    return userFile

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

def histogram(category, countCategory, fileToAppend):
    try:
        histFile = open(fileToAppend,'w')
    except:
        print("Corrupted file")
    else:
        # appends count category to end of file
        myStr = catefory + "'s: "
        for i in 1..countCategory:
            myStr += "*"
        histFile.append(myStr)
        histFile.close()

main()

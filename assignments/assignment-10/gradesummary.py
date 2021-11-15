# Lucía Carrera
# CS 021 A
# Program that reads the entire file and produces a grade summary file.  The summary file will 
# contain a list of each grade and the count of the number of students that received that grade, followed by 
# each grade and a list of students that received that grade.  See the end of this document for a sample input 
# and output file.

def main():
    
    ## PROMPT USER FOR INPUT FILE
    file = input("Please indicate the input file to be used: ")
    try:
        infile=open(file,'r')
        
    # error opening file
    except:
        print("Could not open input file. Exiting now ")

    # if no errors opening file
    else:

        ## DECLARE AND INITIALIZE DICTIONARIES
        grade_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0} 
        students_dict = {'A':[], 'B':[], 'C':[], 'D':[],'F':[]}
        

        ## READ CONTENTS OF INPUT TEXT FILE & FILL DICTIONARIES
        # read first line in file
        line = infile.readline().rstrip()

        # loops until end of page
        while line != '':

            # read info and divide into firstname, lastname and dob
            info = line.split(':')
            info[1] = info[1].strip()

            # update the grade counter with the respective grade the student has
            letter_count = grade_dict[info[1]]
            letter_count += 1
            grade_dict[info[1]] = letter_count

            # include the student in the students dict according to the grade they got
            students_dict[info[1]].append(info[0])

            # read next line
            line = infile.readline().rstrip()
            
                
        # close input file
        infile.close()

        ## CREATE SUMMARY FILE
        try:
            outfile = open('grades_summary.txt','w')
        except:
            print("Could not open output file.")
            
        else:

            # write title
            outfile.write("CS21 Grade Summary\n\n")

            # write number of students who got each letter grade
            for key in grade_dict:
                outfile.write(f"{key}s: {grade_dict[key]}\n")

            # write students receiving each grade
            outfile.write("\nStudents receiving each grade")

            for key in students_dict:
                
                # letter header
                outfile.write(f"\n{key}\n")
                
                # get letter set with all the students that got that grade
                letter_students = students_dict[key]

                # loop through each student to print them out
                for student in letter_students:
                    outfile.write(f"{student}\n")
                
            # close output file
            outfile.close()



main()

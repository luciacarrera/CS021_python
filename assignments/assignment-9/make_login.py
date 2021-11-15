# Lucía Carrera
# CS 021 A
# Program that will read in employee information from a file,
# parse the information, and use that information to
# create login information for each employee


# import statement
import random


def main():
    # ask user for name of input file
    file = input("Please indicate the input file to be used: ")
    try:
        infile=open(file,'r')
        
    # error opening file
    except:
        print("Could not open input file. Exiting now ")

    # if no errors opening file
    else:

        # open output file (placed here becuase if fails makes no sense to do the rest of the code)
        file = input("Please indicate the output file to be used: ")
        
        try:
            outfile=open(file,'w')
        
        # error opening file
        except:
            print("Could not open output file. Exiting now ")

        # if no errors opening file
        else:
                
            # tuple of words
            mywords = ("Otter", "Cow", "Bobcat", "Falcon", "Duck", "Whale", "Owl", "Weasel", "Moose", "Fox")

            # read first line in file
            line = infile.readline().rstrip()

            # loops until end of page
            while line != '':

                # read info and divide into firstname, lastname and dob
                info = line.split(',')

                # create vars for readability and to manage info easier
                firstname = info[0]
                lastname = info[1]
                dob = info[2]

                # make_username -> get year of birth with dob.split (Assuming mm/dd/yyyy format) 
                username = make_user_name(firstname, lastname, dob.split('/')[2])

                # create password
                password = make_password(dob, mywords)

                # string to write in outfile
                mystr = f"{firstname} {lastname}'s username is: {username} password is {password}\n"
                outfile.write(mystr)

                # read next line
                line = infile.readline().rstrip()
                
            # close output and input files
            outfile.close()
            infile.close()
            
    #end of main function


    
# function that creates an employee's user name with their first, last name
# and when they were born
def make_user_name(firstname,lastname, yob):

    # initialization of variables and constants
    username = ""
    USRNAMELEN = 8
    FIRSTLETTER = 0
    
    # remove - ' symbols
    firstname = firstname.replace("'", '')
    firstname = firstname.replace("-", '')
    lastname = lastname.replace("'", '')
    lastname = lastname.replace("-", '')

    # check lastname length to see if special steps must be taken
    if len(lastname) < USRNAMELEN - 1:

        # check to see if first and last name make 8 chars
        if len(firstname) + len(lastname) <= USRNAMELEN:
            username = firstname + lastname + str(yob)
        else:
            CUTOFF = USRNAMELEN - len(lastname)
            username = firstname[FIRSTLETTER:CUTOFF] + lastname + str(yob)

    # normal way
    else:
        username = firstname[FIRSTLETTER] + lastname[FIRSTLETTER:USRNAMELEN -1] + str(yob)

    # username must be in small caps
    return username.lower()



# function that will then create and return the
# starting password for that user
def make_password(dob, mytuple):

    # initialization of variables and constants
    password = ""
    MIN_2DIGS = 10

    # divide dob -> assuming format is mm/dd/yyyy
    dob = dob.split('/')
    month = dob[0]
    day = dob[1]

    # check if month/year at least two digits
    if int(month) < MIN_2DIGS :
        month = "0" + str(month)
    if int(day) < MIN_2DIGS :
        day = "0" + str(day)

    # put it all together and you get the best of both worlds
    password = month + random.choice(mytuple) + day

    return password



main()

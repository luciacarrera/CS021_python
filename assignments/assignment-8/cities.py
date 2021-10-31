# Lucía Carrera
# CS 021 A
# Program that asks user for a city name, compares that value with
#the contents of two text files, and reports each match (if any)

def main():

# end of main function

# function to handle importing file data into a list. 
def file2list(filename):

    # initialization of city list to return empty in case of error
    cities = []
    
    # open filename for reading ()
    try:
        infile = open(filename,'r')
    except:
        print(f"***FILE ERROR: {filename} cannot be found")
        
    # read each city name and store in list if could open file
    else:
        # first city in sheet
        city = infile.readline().rstrip()

        # loops until end of page
        while city != '':
            cities.append(city)

    
    # close file
    infile.close()
    
    # return list
    return cities
    
# end of file2list function

main()

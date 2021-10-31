# Lucía Carrera
# CS 021 A
# Program that asks user for a city name, compares that value with
#the contents of two text files, and reports each match (if any)

def main():
    # initialization of vt and nh lists
    vtlist = file2list('vt_municipalities.txt')
    nhlist = file2list('nh_municipalities.txt')

    # initialization of contstants to know amount of cities in each list
    VTCITIES = len(vtlist)
    NHCITIES = len(nhlist)

    # make sure lists are not empty
    if VTCITIES != 0 and NHCITIES != 0:

        # ask user for city
        name = input("City name (type 'q' to quit): ")
        
        # ask user until they decide to quit
        while name != 'q':

            # check if city is in either list
            if name in vtlist and name in nhlist:
                print(f"{name} is in Vermont and New Hampshire.")
                
            elif name in vtlist:
                print(f"{name} is in Vermont.")
                
            elif name in nhlist:
                print(f"{name} is in New Hampshire.")
                
            else:
                print("Neither VT nor NH has a city by that name.")
            
            # ask user again
            name = input("\nCity name (type 'q' to quit): ")
            
    # if empty do nothing
    
# end of main function

# function to handle importing file data into a list. 
def file2list(filename):

    # initialization of city list to return empty in case of error
    cities = []
    
    # open filename for reading ()
    try:
        infile = open(filename,'r')
    except:
        print(f"***FILE ERROR: {filename} cannot be found.")
        
    # read each city name and store in list if could open file
    else:
        # reads first line in sheet
        city = infile.readline().rstrip()

        # loops until end of page
        while city != '':
            cities.append(city)

            # reads next line
            city = infile.readline().rstrip()

        # close file
        infile.close()
    
    # return list
    return cities
    
# end of file2list function

main()

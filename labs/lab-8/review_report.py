

def main():
    # ask user for file
    file = input("What file should I use? ")
    try:
        infile=open(file,'r')
    except:
        print("Can't open file")
    else:
        n_reviews = 0
        star5 = 0
        star4 = 0
        star3 = 0
        star2 = 0
        star1 = 0
        aline = infile.readlines()

        for line in aline:
            try:
                review = int(line)
            except:
                print("Invalid data removed")
            else:
                if(review == 5):
                    star5 += 1
                elif (review == 4):
                    star4 += 1
                elif (review == 3):
                    star3 += 1
                elif (review == 2):
                    star2 += 1
                else:
                    star1 += 1
                    
                n_reviews += 1

        sum_reviews = star5*5 + star4*4 + star3*3 + star2*2 + star1*1
        print(sum_reviews)
        print(n_reviews)
        average = sum_reviews / n_reviews

        infile.close()

        outfile_name = input("What file name should be used for output? ")
        outfile = open(outfile_name,'w')
        outfile.write(f"Average review is: {average:.2f}\n")
        outfile.close()

        histogram("5", star5, outfile_name) #error
        histogram("4", star4, outfile_name)
        histogram("3", star3, outfile_name)
        histogram("2", star2, outfile_name)
        histogram("1", star1, outfile_name)


def histogram(label, star_count, outfile):
    try: # error
        file = open(outfile, 'a')
    except:
        print("Could not open file")
    else:
        line = label + "-Star Reviews: "
        for i in range(1, star_count):
            line += "*"
        line +="\n"
        file.write(line)
        file.close()
    
main()

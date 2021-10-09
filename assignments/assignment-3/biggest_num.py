# Lucía Carrera
# CS021 A
# Program will sort three int values chosen by the user

# Constants
# no constants because we use the same variables from input to order them

# get num 1
num_1 = int(input("First number? "))

# get num 2
num_2 = int(input("Second number? "))

# get num 3
num_3 = int(input("Third number? "))
           
# sort biggest num between num 1 and num 2
# temp to hold value when sorting
temp = 0

# check if num 2 is bigger than num 1
if num_1 < num_2:
    temp = num_1
    num_1 = num_2
    num_2 = temp

# check if num 3 is bigger than num 1
if num_1 < num_3:
    temp = num_1
    num_1 = num_3
    num_2 = temp
    num_3 = num_2

# check if num 3 is in between num 1 and 2
# using elif because there is two other cases but one just remains the same
elif num_1 >= num_3 and num_2 < num_3:
    temp = num_2
    num_2 = num_3
    num_3 = temp

# if not the numbers stay in the same place

# print output
print("Descending order:", num_1, num_2, num_3)

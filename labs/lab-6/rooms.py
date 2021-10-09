import random
def main():
    for i in range(0,10):
        print(room_draw())

def room_draw():
    campus = ""
    num = random.randint(1,4)
    if( num == 1):
        campus = "University Heights"
    elif num == 2:
        campus = "Main Campus"
    elif num == 3:
        campus = "Athletic Campus"
    else:
        campus = "Trinity Campus"
    return campus

main()

import math

print("Rally's Quadratic Equation Solver\nYou'll be prompted for the coefficents of the equation ax^2 + bx + c = 0.\nThe roots will be computed and displayed.")
a = float(input("a = ? "))
b = float(input("b = ? "))
c = float(input("c = ? "))


discriminant = b**2 -(4*a*c)
print(discriminant)

if discriminant == 0:
    root = -b / (2*a)
    print("The one roots of the equation is {:.1f}".format(root))
elif discriminant < 0:
    print("There are no real roots to this equation")
else:
    root1 = (-b -math.sqrt(discriminant))/ (2*a)
    root2 = (-b +math.sqrt(discriminant))/ (2*a)
    print("The two roots of the equation are {:.1f} and {:.1f}".format(root1,root2))

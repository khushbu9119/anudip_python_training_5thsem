side1 = int(input("enter first side(in CM) : "))
side2 = int(input("enter second side (in CM) : "))
side3 = int(input("enter third side (in CM) : ")) 

#***********PERIMETER***********
perimeter = side1 + side2 + side3
print("Perimeter : ",perimeter,"sq.cm")

#******AREA*******
s = perimeter/2
area = (s*(s-side1)*(s-side2)*(s-side3))**0.5
print("Area : ",area,"sq.cm")
# to import modules
import AreaCalculator

# INPUT THE CHOISE
choise = input("ENTER CHOISE : ")
choise=choise.lower()

# AREA OF RECTANGLE
if choise == "Rectangle":
    length = int(input("Enter length of rectangle (in CM) : "))
    breadth = int(input("Enter breadth of rectangle (in CM) : "))
    # validate length and breadth
    if length < 0 or breadth < 0:
        exit("Length and breadth cannot be negative.")
    rect_area = AreaCalculator.calculate_area(length, breadth)
    rect_perimeter = AreaCalculator.calculate_perimeter(length, breadth)
    # display area and perimeter of rectangle
    print("Area of Rectangle : ", rect_area, "sq.cm")
    print("Perimeter of Rectangle : ", rect_perimeter, "cm")
    print("________________________")

# AREA OF CIRCLE

if choise == "Circle":
    # Circle Area and Circumference
    radius = int(input("Enter radius of circle (in CM) : "))
    if radius < 0:
        exit("Radius cannot be negative.")
    circle_area = AreaCalculator.calculate_circle_area(radius)  
    circle_circumference = AreaCalculator.calculate_circumference(radius)
    print("Area of Circle : ", circle_area, "sq.cm")
    print("Circumference of Circle : ", circle_circumference, "cm")
    print("________________________________")

# AREA OF SQUARE

if choise =="Square":
    # Square Area and Perimeter
    side = int(input("Enter side of square (in CM) : "))
    if side < 0:
        exit("Side cannot be negative.")
    square_area = AreaCalculator.calculate_square_area(side)
    square_perimeter = AreaCalculator.calculate_square_perimeter(side)
    print("Area of Square : ", square_area, "sq.cm")
    print("Perimeter of Square : ", square_perimeter, "cm")
    print("________________________")

# AREA OF RIGHTANGLE TRIANGLE

if choise == "Rigthangle Triangle":
    #Right angle triangle area
    base = int(input("Enter base of right angle triangle (in CM) : "))
    height = int(input("Enter height of right angle triangle (in CM) : "))
    if base < 0 or height < 0:
        exit("Base and height cannot be negative.")
    rightangle_triangle_area = AreaCalculator.calculate_Rightangle_triangle_area(base, height)
    print("Area of Right Angle Triangle : ", rightangle_triangle_area, "sq.cm")
    print("________________________")

# AREA OF TRIANGLE

if choise == "Triangle":
    # Triangle Area and Perimeter
    side1 = int(input("Enter first side of triangle (in CM) : "))
    side2 = int(input("Enter second side of triangle (in CM) : "))
    side3 = int(input("Enter third side of triangle (in CM) : "))   
    if side1 < 0 or side2 < 0 or side3 < 0:
        exit("Sides of triangle cannot be negative.")
    triangle_area = AreaCalculator.calculate_triangle_area(side1, side2, side3)
    triangle_perimeter = AreaCalculator.calculate_triangle_perimeter(side1, side2, side3)   
    print("Area of Triangle : ", triangle_area, "sq.cm")
    print("Perimeter of Triangle : ", triangle_perimeter, "cm")
    print("______________________________")

# EXIT

if choise == "exit":
    exit("Want to exit")
    print("___________________")







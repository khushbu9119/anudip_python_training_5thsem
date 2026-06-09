#Rectangular Area Calculator
def calculate_area(length, breadth):
    #calculate area
    area = length * breadth
    #return the calculated area
    return area
#---------------------------------------------
#Rectangular Perimeter Calculator
def calculate_perimeter(length, breadth):
    #calculate perimeter
    perimeter = 2 * (length + breadth)
    #return the calculated perimeter
    return perimeter    
#Circle Area Calculator
def calculate_circle_area(radius):
    #calculate area
    area = 3.14 * radius * radius
    #return the calculated area
    return area
#Circle Circumference Calculator
def calculate_circumference(radius):
    #calculate circumference
    circumference = 2 * 3.14 * radius
    #return the calculated circumference
    return circumference
#Square Area Calculator
def calculate_square_area(side):
    #calculate area
    area = side * side
    #return the calculated area
    return area
#Square Perimeter Calculator
def calculate_square_perimeter(side):
    #calculate perimeter
    perimeter = 4 * side
    #return the calculated perimeter
    return perimeter
#Triangle Area Calculator
def calculate_Rightangle_triangle_area(base, height):
    #calculate area
    area = 0.5 * base * height
    #return the calculated area
    return area
#Triangle Perimeter Calculator
def calculate_triangle_perimeter(side1, side2, side3):
    #calculate perimeter
    perimeter = side1 + side2 + side3
    #return the calculated perimeter
    return perimeter
#Triangle Area Calculator using Heron's formula
def calculate_triangle_area(side1, side2, side3):
    #calculate semi-perimeter
    s = (side1 + side2 + side3) / 2
    #calculate area using Heron's formula
    area = (s * (s - side1) * (s - side2) * (s - side3)) ** 0.5
    #return the calculated area
    return area


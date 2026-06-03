
# Program to calculate Area and Perimeter with valid

length = float(input("Enter length(in cm): "))
breadth = float(input("Enter breadth (in cm): "))

if (length > 0 and breadth > 0):
    area = length * breadth
    perimeter = 2 * (length + breadth)

    print("Area =", area,"sq.cm")
    print("Perimeter =", perimeter,"cm")
else:
    print("Please enter valid positive values")
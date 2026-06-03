# Program to check whether three sides can form a triangle or not

a = float(input("Enter first side: "))
if(a<=0):
    exit("side greater than zero")

#__________________________________________

b = float(input("Enter second side: "))
if(b<=0):
    exit("side greater than zero")

#______________________________________________

c = float(input("Enter third side: "))
if(c<=0):
    exit("side greater than zero")

#_____________________________________________


# Triangle condition
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Triangle can be formed")
    if (a == b == c):
        print("It is an Equilateral Triangle")

    if( a == b or b == c or a == c):
        if (a*a + b*b == c*c) or (a*a + c*c == b*b) or (b*b + c*c == a*a):
            print("Right Isosceles Triangle")

        # Acute Isosceles
        elif (a*a + b*b > c*c) and (a*a + c*c > b*b) and (b*b + c*c > a*a):
            print("Acute Isosceles Triangle")

        # Obtuse Isosceles
        else:
            print("Obtuse Isosceles Triangle")

    else:
        print("It is a Scalene Triangle")
else:
    print("Triangle cannot be formed")
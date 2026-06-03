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
else:
    print("Triangle cannot be formed")
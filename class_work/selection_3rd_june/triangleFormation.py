angle1 = float(input("Enter the first angle"))
if(angle1 <=0 ):
    exit("Angle must be positive")
#__________________________________

angle2 = float(input("Enter the second angle"))
if(angle2 <= 0):
    exit("Angle must be positive")
    #__________________________________

angle3 = float(input("Enter the third angle"))
if(angle3 <= 0):
    exit("Angle must be positive")


#***************verifiy triangle formation


if(angle1+angle2+angle3 == 180):
    print("above angle formed triangle")
else:
    print("Above angle dose not formed triangle")
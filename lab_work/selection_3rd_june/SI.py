# Simple Interest 

p = int(input("Enter principal amount: "))
if(p<=0):
    exit("can't be negative......exited")
r = int(input("Enter rate of interest: "))
if(r<=0):
    exit("can't be negative......exited")
t = int(input("Enter time: "))
if(t<=0):
    exit("can't be negative......exited")

#***************calculate si********
    si = (p * r * t) / 100
    print("Simple Interest =", si)

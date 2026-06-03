second = int(input("enter the time : "))

#***********check second*******
if(second < 0):
    exit("Time can't be negative......exited ")

print("________________________")

hour = 0
minute = 0

#********convert second into hour************


if(second>=3600):
    hour = second // 3600
    second = second % 3600


 #******************convert second minute***********

if(second >= 60):
    minute = second // 60
    second = second % 60


print("equivalent time :",hour,"hour",minute,"minute",second,"second")





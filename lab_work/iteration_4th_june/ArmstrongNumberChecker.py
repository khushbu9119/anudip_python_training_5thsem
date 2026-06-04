# Program to check if a number is an Armstrong Number or not
num = int(input("Enter a number: "))

temp = num
sum = 0
# Calculate the sum of the cubes of the digits
while temp > 0:
    digit = temp % 10
    sum = sum + (digit ** 3)
    temp = temp // 10
# Check if the sum is equal to the original number
if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is Not an Armstrong Number")
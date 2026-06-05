# Program to check whether a number is a Strong Number or not

# Taking input from user
num = int(input("Enter a number: "))

# Storing original number for comparison later
original_num = num

# Variable to store sum of factorials of digits
sum_factorial = 0

# Loop runs until number becomes 0
while num > 0:

    # Extracting last digit
    digit = num % 10

    # Finding factorial of the digit
    factorial = 1

    # Loop to calculate factorial
    for i in range(1, digit + 1):
        factorial = factorial * i

    # Adding factorial to total sum
    sum_factorial = sum_factorial + factorial

    # Removing last digit from number
    num = num // 10

# Checking whether sum of factorials equals original number
if sum_factorial == original_num:
    print(original_num, "is a Strong Number")
else:
    print(original_num, "is not a Strong Number")
# Program to check consecutive digit number
# without using flag

num = input("Enter a number: ")

for i in range(len(num) - 1):

    current_digit = int(num[i])
    next_digit = int(num[i + 1])

    # Check if next digit is not 1 greater
    if (next_digit != current_digit + 1):
        print(num, "is NOT a Consecutive Digit Number")
        break

else:
    # Executes only if loop completes without break
    print(num, "is a Consecutive Digit Number")
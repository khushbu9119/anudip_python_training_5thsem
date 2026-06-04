pin = int(input("Enter your 4-digit PIN: "))
correct_pin = 1234
while (pin != correct_pin):
    print("Incorrect PIN. Please try again.")
    pin = int(input("Enter your 4-digit PIN: "))
print("PIN verified successfully. Access granted.")
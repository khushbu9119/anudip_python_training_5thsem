#********** PIN Verification Program *********
pin = int(input("Enter your 4-digit PIN: "))
correct_pin = 1234
# *************Verify the PIN************
while (pin != correct_pin):
    print("Incorrect PIN. Please try again.")
    pin = int(input("Enter your 4-digit PIN: "))
#**********PIN verified successfully. Access granted.************
print("PIN verified successfully. Access granted.")
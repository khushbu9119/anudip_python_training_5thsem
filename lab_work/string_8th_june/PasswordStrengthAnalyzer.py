# Input password
password = "Python@2026!"

# Variables
upper = 0
lower = 0
digits = 0
special = 0

digit_list = []
special_list = []

# Check every character
for ch in password:

    # Count uppercase letters
    if ch.isupper():
        upper += 1

    # Count lowercase letters
    elif ch.islower():
        lower += 1

    # Count digits
    elif ch.isdigit():
        digits += 1
        digit_list.append(ch)

    # Count special characters
    else:
        special += 1
        special_list.append(ch)

# Check password strength
if len(password) >= 8 and upper >= 1 and lower >= 1 and digits >= 1 and special >= 1:
    strength = "Strong"

elif len(password) >= 6:
    strength = "Medium"

else:
    strength = "Weak"

# Display result
print("Password:", password)
print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
print("Digits:", digits)
print("Special Characters:", special)
print("Digits Found:", digit_list)
print("Special Characters Found:", special_list)
print("Password Strength:", strength)
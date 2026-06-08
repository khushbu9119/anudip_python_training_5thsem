# Vehicle number
vehicle = "MH12AB4589"

# Extract details
state = vehicle[:2]
district = vehicle[2:4]
series = vehicle[4:6]
number = vehicle[6:]

# Variables
letters = 0
digits = 0

# Count letters and digits
for ch in vehicle:

    if ch.isalpha():
        letters += 1

    elif ch.isdigit():
        digits += 1

# Assume valid
valid = True

# Validation checks
if not vehicle[:2].isalpha():
    valid = False

if not vehicle[2:4].isdigit():
    valid = False

if not vehicle[4:6].isalpha():
    valid = False

if not vehicle[6:].isdigit():
    valid = False

# Display result
print("Vehicle Number:", vehicle)
print("State Code:", state)
print("District Code:", district)
print("Series:", series)
print("Vehicle Number:", number)
print("Total Letters:", letters)
print("Total Digits:", digits)

# Display validity
if valid:
    print("Vehicle Number Status: Valid")

else:
    print("Vehicle Number Status: Invalid")
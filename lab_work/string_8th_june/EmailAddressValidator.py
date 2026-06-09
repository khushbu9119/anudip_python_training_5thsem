# Input email
email = "rahul.sharma2026@gmail.com"

# Extract username
username = email.split("@")[0]

# Extract domain
domain = email.split("@")[1].split(".")[0]

# Extract extension
extension = email.split(".")[-1]

# Variables
digit_count = 0
special_count = 0

# Count digits in username
for ch in username:
    if ch.isdigit():
        digit_count += 1

# Count special characters
for ch in email:
    if not ch.isalnum():
        special_count += 1

# Assume valid
valid = True

# Check only one @ exists
if email.count("@") != 1:
    valid = False

# Check dot exists after @
if "." not in email.split("@")[1]:
    valid = False

# Display result
print("Email:", email)
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)
print("Digits Found:", digit_count)
print("Special Characters Found:", special_count)

# Display validity
if valid:
    print("Email Status: Valid")

else:
    print("Email Status: Invalid")
# License key
key = "ABCD-EFGH-IJKL-MNOP"

# Split into groups
groups = key.split("-")

# Variables
letters = 0
vowels = 0

# Count letters and vowels
for ch in key:

    if ch.isalpha():
        letters += 1

        if ch.lower() in "aeiou":
            vowels += 1

# Remove hyphens
merged = key.replace("-", "")

# Assume valid
valid = True

# Check total groups
if len(groups) != 4:
    valid = False

# Check each group length
for g in groups:

    if len(g) != 4:
        valid = False

# Display result
print("Groups:", groups)
print("Number of Groups:", len(groups))
print("Total Letters:", letters)
print("Total Vowels:", vowels)
print("Merged Key:", merged)

# Display validity
if valid:
    print("License Key Status: Valid")

else:
    print("License Key Status: Invalid")
# Original name
name = "Rahul Sharma"

# Remove spaces and convert to lowercase
username = name.replace(" ", "").lower()

# Append year
username = username + "2026"

# Keep only first 12 characters
if len(username) > 12:
    username = username[:12]

# Variables
vowels = 0
consonants = 0

# Count vowels and consonants
for ch in username:

    if ch.isalpha():

        if ch in "aeiou":
            vowels += 1

        else:
            consonants += 1

# Display result
print("Original Name:", name)
print("Generated Username:", username)
print("Username Length:", len(username))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Status: Username Generated Successfully")
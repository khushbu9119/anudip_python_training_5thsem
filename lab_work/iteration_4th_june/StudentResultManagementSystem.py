# Student Result Management System

total = 0
fail_count = 0

# Get marks for 5 subjects

for i in range(1, 6):
    marks = int(input(f"Enter marks of Subject {i}: "))
    
    total = total + marks

    if marks < 40:
        fail_count += 1
# Calculate percentage and grade

percentage = total / 5

# Determine grade based on percentage

if percentage >= 90:
    grade = "A+"

elif percentage >= 75:
    grade = "A"

elif percentage >= 60:
    grade = "B"

elif percentage >= 40:
    grade = "C"

else:
    grade = "Fail"

# Display the results

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Number of Subjects Failed:", fail_count)
# Sample Data
quiz_scores = {
    "S001": 18,
    "S002": 12,
    "S003": 9,
    "S004": 20,
    "S005": 14,
    "S006": 7,
    "S007": 16,
    "S008": 10,
    "S009": 19,
    "S010": 13
}

# Display students scoring 15 or above
print("Students scoring 15 or above:")

for student, marks in quiz_scores.items():
    if marks >= 15:
        print(student, ":", marks)

# Count students scoring below 10
count = 0

for marks in quiz_scores.values():
    if marks < 10:
        count += 1

print("\nStudents scoring below 10:", count)

# Find the top performer
highest_marks = max(quiz_scores.values())

for student, marks in quiz_scores.items():
    if marks == highest_marks:
        print("\nTop Performer:")
        print(student, ":", marks)

# Create list of students who passed
passed_students = []

for student, marks in quiz_scores.items():
    if marks >= 10:
        passed_students.append(student)

print("\nStudents who passed:")
print(passed_students)

# Calculate class average
total = 0

for marks in quiz_scores.values():
    total += marks

average = total / len(quiz_scores)

print("\nClass Average:", average)
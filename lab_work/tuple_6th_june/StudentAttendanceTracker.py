# Problem Statement
# Attendance for 15 days is recorded as:
# attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']
# Write a program to:
# • Count present and absent days.
# • Calculate attendance percentage.
# • Determine eligibility (minimum 75% attendance).
# • Display positions where the student was absent.



# Attendance list
attendance = ['P', 'P', 'A', 'P', 'A', 'P', 'P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P']

# Count present and absent days
present = 0
absent = 0

for i in attendance:
    if i == 'P':
        present += 1
    else:
        absent += 1

# Calculate attendance percentage
total_days = len(attendance)
percentage = (present / total_days) * 100

# Display counts
print("Present Days =", present)
print("Absent Days =", absent)

# Display attendance percentage
print("Attendance Percentage =", percentage, "%")

# Check eligibility
if percentage >= 75:
    print("Eligible for Exam")
else:
    print("Not Eligible for Exam")

# Display positions where student was absent
print("Absent on positions:")

for i in range(total_days):
    if attendance[i] == 'A':
        print(i)
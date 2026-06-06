# Attendance Tracker Using Dictionary

attendance = {}

# Input attendance of 30 students

for i in range(5):

    roll = int(input("Enter Roll Number : "))
    status = input("Enter Attendance (Present/Absent) : ")

    attendance[roll] = status

print("----------------------")

# Display roll numbers of present students

print("Students who are Present")

for roll in attendance:

    if attendance[roll].lower() == "present":
        print("Roll Number :", roll)
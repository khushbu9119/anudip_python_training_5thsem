# Employee Performance Evaluation
# Problem Statement
# A company stores employee details in a tuple. Each employee record contains:
# employees = ( ("E101", "Anuj", 92), ("E102", "Rahul", 76), ("E103", "Priya", 58), ("E104", "Neha", 88), ("E105", "Amit", 45) )
# Where:
# First value = Employee ID
# Second value = Employee Name
# Third value = Performance Score
# Tasks
# Write a Python program to:
# 1.Display details of employees scoring 80 or above.
# 2.Count the number of employees who need improvement (score below 60).
# 3.Find the employee with the highest score.
# 4.Create a list containing the names of all employees scoring above 75.
# 5.Display the performance category for each employee:
# o 90 and above → Excellent
# o 75 to 89 → Good
# o 60 to 74 → Average
# o Below 60 → Needs Improvement


#-----------------------------------------------

# Employee data
employees = (
    ("E101", "Anuj", 92),
    ("E102", "Rahul", 76),
    ("E103", "Priya", 58),
    ("E104", "Neha", 88),
    ("E105", "Amit", 45)
)
#-----------------------------------------------
# Task 1: Display details of employees scoring 80 or above.
for emp in employees:
    if emp[2] >= 80:
        print("Employee ID: " ,emp[0])
        print("Name: " ,emp[1])
        print("Score: " ,emp[2])
print("--------------------------------")

#-----------------------------------------------
# Task 2: Count the number of employees who need improvement (score below 60).
count = 0
for emp in employees:
    if emp[2] < 60:
        count += 1
print(f"Number of employees who need improvement: {count}")
print("--------------------------------")
#-----------------------------------------------
# Task 3: Find the employee with the highest score.
highest_score = 0
topEmployee = None
for emp in employees:
    if emp[2] > highest_score:
        highest_score = emp[2]
        topEmployee = emp
print("Top Employee :", topEmployee[1])
print("Highest Score :", highest_score)
print("--------------------------------")
#-----------------------------------------------
# Task 4: Create a list containing the names of all employees scoring above 75.
good_performers = []
for emp in employees:
    if emp[2] > 75:
        good_performers.append(emp[1])
print("Employees scoring above 75:", good_performers)
print("--------------------------------")
#-----------------------------------------------
# Task 5: Display the performance category for each employee
for emp in employees:
    if emp[2] >= 90:
        category = "Excellent"
    elif emp[2] >= 75:
        category = "Good"
    elif emp[2] >= 60:
        category = "Average"
    else:
        category = "Needs Improvement"
    print("Employee ID :", emp[0])
    print("Name :", emp[1])
    print("Score :", emp[2])
    print("Performance Category :", category)

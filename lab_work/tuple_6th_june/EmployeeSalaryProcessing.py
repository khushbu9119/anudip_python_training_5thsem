# Employee data is stored as tuples:
# employees = [ ("Rahul", 35000), 
#               ("Priya", 55000), 
#               ("Amit", 42000), 
#               ("Neha", 65000) ]
# Write a program to:
# • Display employees earning above ₹50,000.
# • Find the highest-paid employee.
# • Calculate total salary expenditure.
# • Count employees earning below ₹40,000.


# Employee Salary Analysis

employees = [
    ("Rahul", 35000),
    ("Priya", 55000),
    ("Amit", 42000),
    ("Neha", 65000)
]

# ------------------------------------------------
# Task 1: Display employees earning above ₹50,000

print("Employees earning above ₹50,000")

for emp in employees:
    if emp[1] > 50000:
        print("Name :", emp[0])
        print("Salary : ₹", emp[1])
        print("----------------------")

# ------------------------------------------------
# Task 2: Find the highest-paid employee

top_employee = employees[0]

for emp in employees:
    if emp[1] > top_employee[1]:
        top_employee = emp

print("Highest Paid Employee :", top_employee[0])
print("Highest Salary : ₹", top_employee[1])
print("----------------------")

# ------------------------------------------------
# Task 3: Calculate total salary expenditure

total_salary = 0

for emp in employees:
    total_salary += emp[1]

print("Total Salary Expenditure : ₹", total_salary)

print("----------------------")

# ------------------------------------------------
# Task 4: Count employees earning below ₹40,000

count = 0

for emp in employees:
    if emp[1] < 40000:
        count += 1

print("Employees earning below ₹40,000 :", count)
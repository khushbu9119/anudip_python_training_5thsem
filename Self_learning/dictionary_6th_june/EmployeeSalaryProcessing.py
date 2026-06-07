# Sample Data
salary = {
    "EMP101": 45000,
    "EMP102": 62000,
    "EMP103": 38000,
    "EMP104": 75000,
    "EMP105": 54000,
    "EMP106": 29000,
    "EMP107": 82000,
    "EMP108": 48000,
    "EMP109": 36000,
    "EMP110": 68000
}

# Display employees earning above ₹60,000
print("Employees earning above ₹60,000:")

for emp, sal in salary.items():
    if sal > 60000:
        print(emp, ":", sal)

# Count employees earning below ₹40,000
count = 0

for sal in salary.values():
    if sal < 40000:
        count += 1

print("\nEmployees earning below ₹40,000:", count)

# Find highest-paid employee
highest_salary = max(salary.values())

for emp, sal in salary.items():
    if sal == highest_salary:
        print("\nHighest Paid Employee:")
        print(emp, ":", sal)

# Create list of employees eligible for bonus
bonus_list = []

for emp, sal in salary.items():
    if sal > 50000:
        bonus_list.append(emp)

print("\nEmployees eligible for bonus:")
print(bonus_list)

# Calculate average salary
total = 0

for sal in salary.values():
    total += sal

average = total / len(salary)

print("\nAverage Salary:", average)
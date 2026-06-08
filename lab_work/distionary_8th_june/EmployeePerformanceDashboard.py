# Employee performance scores are stored as:
# performance = { "EMP101": 92, "EMP102": 78, "EMP103": 45, "EMP104": 88, "EMP105": 97, "EMP106": 56, "EMP107": 81, "EMP108": 64, "EMP109": 39, "EMP110": 73 }
# Tasks
# 1.
# Display employees scoring above 80.
# 2.
# Count employees needing improvement (score < 60).
# 3.
# Find the top performer.
# 4.
# Calculate average performance score.
# 5.
# Create separate lists:
# o
# Excellent (≥ 90)
# o
# Good (75–89)
# o
# Average (60–74)
# o
# Poor (< 60)

# Sample Data
performance = {
    "EMP101": 92,
    "EMP102": 78,
    "EMP103": 45,
    "EMP104": 88,
    "EMP105": 97,
    "EMP106": 56,
    "EMP107": 81,
    "EMP108": 64,
    "EMP109": 39,
    "EMP110": 73
}   
# Display employees scoring above 80
print("Employees scoring above 80:")
for emp_id, score in performance.items():
    if score > 80:
        print(emp_id, ":", score)
print("--------------------------------------------")
# Count employees needing improvement (score < 60)
improvement_count = 0
for score in performance.values():
    if score < 60:
        improvement_count += 1
print("Number of employees needing improvement:", improvement_count)
print("--------------------------------------------")
# Find the top performer
top_emp = ""
top_score = 0

for emp, score in performance.items():
    if score > top_score:
        top_score = score
        top_emp = emp
print("Top Performer:", top_emp, "-", top_score)    
print("--------------------------------------------")
# Calculate average performance score
total_score = 0
for score in performance.values():
    total_score += score
average_score = total_score / len(performance)
print("Average Performance Score:", average_score)
print("--------------------------------------------")
# Create separate lists for performance categories
excellent_employees = []
good_employees = []
average_employees = []
poor_employees = []
for emp, score in performance.items():
    if score >= 90:
        excellent_employees.append(emp)
    elif score >= 75 and score < 90:
        good_employees.append(emp)
    elif score >= 60 and score < 75:
        average_employees.append(emp)
    else:
        poor_employees.append(emp)
print("Excellent Employees:", excellent_employees)
print("Good Employees:", good_employees)    
print("Average Employees:", average_employees)
print("Poor Employees:", poor_employees)
print("--------------------------------------------")
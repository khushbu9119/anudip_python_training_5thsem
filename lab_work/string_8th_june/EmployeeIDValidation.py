# Employee ID Program

emp_id = "EMP2026ANUJ458"

# 1. Count uppercase letters
upper_count = 0
for ch in emp_id:
    if ch.isupper():
        upper_count += 1

# 2. Count digits
digit_count = 0
for ch in emp_id:
    if ch.isdigit():
        digit_count += 1

# 3. Extract joining year
year = emp_id[3:7]

# 4. Extract employee name
name = emp_id[7:-3]

# 5. Check ID rules
valid = True

# Rule 1: Starts with EMP
if emp_id[:3] != "EMP":
    valid = False

# Rule 2: Exactly 4 digits for year
if not emp_id[3:7].isdigit():
    valid = False

# Rule 3: Ends with exactly 3 digits
if not emp_id[-3:].isdigit():
    valid = False

# 6. Create list of digits
digit_list = []

for ch in emp_id:
    if ch.isdigit():
        digit_list.append(int(ch))

# 7. Find sum of digits
digit_sum = 0

for num in digit_list:
    digit_sum += num

# 8. Display result
print("Employee ID:", emp_id)
print("Uppercase Letters:", upper_count)
print("Digits:", digit_count)
print("Joining Year:", year)
print("Employee Name:", name)
print("Digit List:", digit_list)
print("Sum of Digits:", digit_sum)

if valid:
    print("ID Status: Valid")
else:
    print("ID Status: Invalid")
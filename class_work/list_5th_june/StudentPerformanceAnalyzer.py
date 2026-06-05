
# List of student marks
marks = [78, 45, 92, 35, 88, 40, 99, 56]

#  Display all passed students (marks >= 40)
print("Passed Students Marks:")
for i in marks:
    if i >= 40:
        print(i)

#  Count the number of failed students
fail_count = 0

for i in marks:
    if i < 40:
        fail_count += 1

print("Number of Failed Students:", fail_count)

#  Find highest and lowest marks without using max() or min()

highest = marks[0]
lowest = marks[0]

for i in marks:
    if i > highest:
        highest = i

    if i < lowest:
        lowest = i

print("Highest Marks:", highest)
print("Lowest Marks:", lowest)

#  Create a new list containing marks above 75

above_75 = []

for i in marks:
    if i > 75:
        above_75.append(i)

print("Marks Above 75:", above_75)
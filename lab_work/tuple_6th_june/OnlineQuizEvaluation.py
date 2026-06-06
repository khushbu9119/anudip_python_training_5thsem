# Problem Statement
# Correct answers:
# correct = ['A', 'C', 'B', 'D', 'A']
# Student answers:
# student = ['A', 'B', 'B', 'D', 'C']
# Write a program to:
# • Calculate score.
# • Display incorrectly answered question numbers.
# • Count correct and wrong answers.
# • Determine pass/fail (minimum 60%).


# Correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# Student answers
student = ['A', 'B', 'B', 'D', 'C']

# Variables
score = 0
wrong = 0

print("Incorrectly Answered Question Numbers:")

# Checking answers
for i in range(len(correct)):
    
    if correct[i] == student[i]:
        score += 1
    else:
        wrong += 1
        print(i + 1)

# Count correct answers
correct_count = score

# Calculate percentage
percentage = (score / len(correct)) * 100

# Display result
print("Correct Answers =", correct_count)
print("Wrong Answers =", wrong)
print("Score =", score)
print("Percentage =", percentage, "%")

# Pass or Fail
if percentage >= 60:
    print("Pass")
else:
    print("Fail")
# Sample Data
scores = {
    "Virat": 78,
    "Rohit": 112,
    "Gill": 45,
    "Rahul": 89,
    "Hardik": 32,
    "Jadeja": 61,
    "Surya": 105,
    "Pant": 95,
    "Bumrah": 18,
    "Shami": 25
}

# Display players who scored 50 or more runs
print("Players who scored 50 or more runs:")

for player, run in scores.items():
    if run >= 50:
        print(player, ":", run)

# Count the number of centuries
century_count = 0

for run in scores.values():
    if run >= 100:
        century_count += 1

print("\nNumber of centuries:", century_count)

# Find the player with the highest score
highest_score = max(scores.values())

for player, run in scores.items():
    if run == highest_score:
        print("\nPlayer with highest score:")
        print(player, ":", run)

# Create list of players scoring below 30 runs
low_scores = []

for player, run in scores.items():
    if run < 30:
        low_scores.append(player)

print("\nPlayers scoring below 30 runs:")
print(low_scores)

# Determine players scoring between 50 and 99
count = 0

for run in scores.values():
    if run >= 50 and run <= 99:
        count += 1

print("\nPlayers scoring between 50 and 99:", count)
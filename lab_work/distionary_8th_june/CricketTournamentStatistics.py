# Problem Statement
# Runs scored by players in a tournament:
# runs = { "Virat": 645, "Rohit": 512, "Gill": 698, "Rahul": 435, "Hardik": 278, "Pant": 534, "Surya": 389, "Jadeja": 301, "Iyer": 455, "KL": 410 }
# Tasks
# 1.
# Display players scoring more than 500 runs.
# 2.
# Find the Orange Cap winner.
# 3.
# Find the lowest scorer.
# 4.
# Calculate total runs scored.
# 5.
# Create a list of players scoring below 400.
# 6.
# Count players scoring between 400 and 600 runs.

runs = {
    "Virat": 645,
    "Rohit": 512,
    "Gill": 698,
    "Rahul": 435,
    "Hardik": 278,
    "Pant": 534,
    "Surya": 389,
    "Jadeja": 301,
    "Iyer": 455,
    "KL": 410
}
# Display players scoring more than 500 runs
print("Players scoring more than 500 runs:")
for player, score in runs.items():
    if score > 500:
        print(player)
print("--------------------------------------------")
# Find the Orange Cap winner
orange_cap_winner = ""
max_runs = 0
for player, score in runs.items():
    if score > max_runs:
        max_runs = score
        orange_cap_winner = player
print("Orange Cap Winner:", orange_cap_winner, "(", max_runs, " runs )")
print("--------------------------------------------")
# Find the lowest scorer
lowest_scorer = ""
min_runs = float('inf')
for player, score in runs.items():
    if score < min_runs:
        min_runs = score
        lowest_scorer = player
print("Lowest Scorer:", lowest_scorer, "(", min_runs, " runs )")
print("--------------------------------------------")
# Calculate total runs scored
total_runs = 0
for score in runs.values():
    total_runs += score
print("Total Runs Scored:", total_runs)
print("--------------------------------------------")
# Create a list of players scoring below 400
players_below_400 = []
for player, score in runs.items():
    if score < 400:
        players_below_400.append(player)
print("Players scoring below 400 runs:")
print(players_below_400)
print("--------------------------------------------")
# Count players scoring between 400 and 600 runs
count_400_600 = 0
for score in runs.values():
    if 400 <= score <= 600:
        count_400_600 += 1
print("Number of players scoring between 400 and 600 runs:", count_400_600)
print("--------------------------------------------")

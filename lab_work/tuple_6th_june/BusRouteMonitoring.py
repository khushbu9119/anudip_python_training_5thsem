# Problem Statement
# Passenger count at each stop:
# passengers = [12, 18, 25, 30, 28, 15, 8]
# Write a program to:
# • Find the busiest stop.
# • Display stops with fewer than 10 passengers.
# • Calculate average passengers.
# • Determine whether any stop exceeded 25 passengers.



# Passenger count at each stop
passengers = [12, 18, 25, 30, 28, 15, 8]

# Find busiest stop
print("Busiest Stop =", passengers.index(max(passengers)))
print("Maximum Passengers =", max(passengers))

# Stops with fewer than 10 passengers
print("Stops with fewer than 10 passengers:")

for i in range(len(passengers)):
    if passengers[i] < 10:
        print(i)

# Average passengers
average = sum(passengers) / len(passengers)

print("Average Passengers =", average)

# Check if any stop exceeded 25 passengers
if max(passengers) > 25:
    print("A stop exceeded 25 passengers")
else:
    print("No stop exceeded 25 passengers")
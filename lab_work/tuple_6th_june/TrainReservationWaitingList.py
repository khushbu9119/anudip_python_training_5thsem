# Problem Statement
# Passenger records:
# passengers = [ ("Anuj", "Confirmed"), ("Rahul", "Waiting"), ("Priya", "Confirmed"), ("Amit", "Waiting"), ("Neha", "Confirmed") ]
# Write a program to:
# • Display all waiting-list passengers.
# • Count confirmed and waiting passengers.
# • Find whether a specific passenger has a confirmed ticket.
# • Create separate lists for confirmed and waiting passengers.

# Passenger Ticket Analysis


passengers = [
    ("Anuj", "Confirmed"),
    ("Rahul", "Waiting"),
    ("Priya", "Confirmed"),
    ("Amit", "Waiting"),
    ("Neha", "Confirmed")
]

# ------------------------------------------------
# Task 1: Display all waiting-list passengers

print("Waiting List Passengers")

for passenger in passengers:
    if passenger[1] == "Waiting":
        print(passenger[0])

print("----------------------")

# ------------------------------------------------
# Task 2: Count confirmed and waiting passengers

confirmed = 0
waiting = 0

for passenger in passengers:

    if passenger[1] == "Confirmed":
        confirmed += 1

    else:
        waiting += 1

print("Confirmed Passengers :", confirmed)
print("Waiting Passengers :", waiting)

print("----------------------")

# ------------------------------------------------
# Task 3: Find whether a specific passenger has a confirmed ticket

name = input("Enter passenger name : ")

found = 0

for passenger in passengers:

    if passenger[0] == name and passenger[1] == "Confirmed":
        found = 1
        break

if found == 1:
    print(name, "has a confirmed ticket")

else:
    print(name, "does not have a confirmed ticket")

print("----------------------")

# ------------------------------------------------
# Task 4: Create separate lists for confirmed and waiting passengers

confirmed_list = []
waiting_list = []

for passenger in passengers:

    if passenger[1] == "Confirmed":
        confirmed_list.append(passenger[0])

    else:
        waiting_list.append(passenger[0])

print("Confirmed Passengers :", confirmed_list)
print("Waiting Passengers :", waiting_list)
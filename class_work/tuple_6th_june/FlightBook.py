# Problem Statement
# A flight reservation system stores passenger records as tuples:
# bookings = ( ("P101", "Delhi", "Confirmed"), ("P102", "Mumbai", "Waiting"), ("P103", "Delhi", "Confirmed"), ("P104", "Chennai", "Cancelled"), ("P105", "Mumbai", "Confirmed"), ("P106", "Delhi", "Waiting") )
# Where:
# • Passenger ID
# • Destination
# • Booking Status
# Tasks
# Write a Python program to:
# 1.Display all passengers whose booking status is Confirmed.
# 2.Count the number of passengers travelling to Delhi.
# 3.Count Confirmed, Waiting, and Cancelled bookings separately.
# 4.Create a list containing passenger IDs with Waiting status.
# 5.Determine which destination has the highest number of bookings.

# Flight Reservation System Using Tuples

bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# ------------------------------------------------
# Task 1: Display all passengers whose booking status is Confirmed

print("----- Confirmed Passengers -----")

for passenger in bookings:
    if passenger[2] == "Confirmed":
        print("Passenger ID :", passenger[0])
        print("Destination :", passenger[1])
        print("Status :", passenger[2])
        print("----------------------------")

# ------------------------------------------------
# Task 2: Count the number of passengers travelling to Delhi

delhi_count = 0

for passenger in bookings:
    if passenger[1] == "Delhi":
        delhi_count += 1

print("Passengers travelling to Delhi :", delhi_count)

print("----------------------------")

# ------------------------------------------------
# Task 3: Count Confirmed, Waiting, and Cancelled bookings separately

confirmed = 0
waiting = 0
cancelled = 0

for passenger in bookings:
    
    if passenger[2] == "Confirmed":
        confirmed += 1

    elif passenger[2] == "Waiting":
        waiting += 1

    elif passenger[2] == "Cancelled":
        cancelled += 1

print("Confirmed Bookings :", confirmed)
print("Waiting Bookings :", waiting)
print("Cancelled Bookings :", cancelled)

print("----------------------------")

# ------------------------------------------------
# Task 4: Create a list containing passenger IDs with Waiting status

waiting_list = []

for passenger in bookings:
    if passenger[2] == "Waiting":
        waiting_list.append(passenger[0])

print("Waiting Passenger IDs :", waiting_list)

print("----------------------------")

# ------------------------------------------------
# Task 5: Determine which destination has the highest number of bookings

delhi = 0
mumbai = 0
chennai = 0

for passenger in bookings:

    if passenger[1] == "Delhi":
        delhi += 1

    elif passenger[1] == "Mumbai":
        mumbai += 1

    elif passenger[1] == "Chennai":
        chennai += 1

if delhi > mumbai and delhi > chennai:
    print("Highest bookings destination : Delhi")

elif mumbai > delhi and mumbai > chennai:
    print("Highest bookings destination : Mumbai")

else:
    print("Highest bookings destination : Chennai")

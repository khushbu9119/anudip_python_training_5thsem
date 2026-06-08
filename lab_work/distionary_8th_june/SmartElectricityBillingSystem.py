# Problem Statement
# Monthly electricity consumption (units) is stored as:
# units = { "House101": 320,
# "House102": 180, "House103": 510, "House104": 275, "House105": 150, "House106": 430, "House107": 220, "House108": 390, "House109": 145, "House110": 600 }
# Tasks
# 1.
# Display houses consuming more than 400 units.
# 2.
# Find the highest-consuming house.
# 3.
# Find the lowest-consuming house.
# 4.
# Calculate total units consumed.
# 5.
# Create lists:
# o
# Low Consumption (< 200)
# o
# Medium Consumption (200–400)
# o
# High Consumption (> 400)
# 6.
# Count houses eligible for an energy-saving campaign (consumption > 300).

units = {
    "House101": 320,
    "House102": 180,
    "House103": 510,
    "House104": 275,
    "House105": 150,
    "House106": 430,
    "House107": 220,
    "House108": 390,
    "House109": 145,
    "House110": 600
}
# Display houses consuming more than 400 units
print("Houses consuming more than 400 units:")
for house, consumption in units.items():
    if consumption > 400:
        print(house)
print("--------------------------------------------")
# Find the highest-consuming house
highest_house = ""
max_consumption = 0
for house, consumption in units.items():
    if consumption > max_consumption:
        max_consumption = consumption
        highest_house = house
print("Highest Consuming House:", highest_house, "(", max_consumption, " units )")
print("--------------------------------------------")
# Find the lowest-consuming house
lowest_house = ""
min_consumption = float('inf')
for house, consumption in units.items():
    if consumption < min_consumption:
        min_consumption = consumption
        lowest_house = house
print("Lowest Consuming House:", lowest_house, "(", min_consumption, " units )")
print("--------------------------------------------")   
# Calculate total units consumed
total_consumption = 0
for consumption in units.values():
    total_consumption += consumption
print("Total Units Consumed:", total_consumption)
print("--------------------------------------------")
# Create lists:
low_consumption = []
medium_consumption = []
high_consumption = []
for house, consumption in units.items():
    if consumption < 200:
        low_consumption.append(house)
    elif 200 <= consumption <= 400:
        medium_consumption.append(house)
    else:
        high_consumption.append(house)

print("Low Consumption (< 200):", low_consumption)
print("Medium Consumption (200–400):", medium_consumption)
print("High Consumption (> 400):", high_consumption)
print("--------------------------------------------")
# Count houses eligible for an energy-saving campaign (consumption > 300)
campaign_count = 0
for consumption in units.values():
    if consumption > 300:
        campaign_count += 1
print("Number of houses eligible for energy-saving campaign:", campaign_count)
print("--------------------------------------------")

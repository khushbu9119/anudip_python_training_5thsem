# Problem Statement
# Daily temperatures of different cities are stored as:
# temperature = { "Delhi": 41, "Mumbai": 33, "Chennai": 37, "Kolkata": 39, "Bengaluru": 28, "Pune": 30, "Jaipur": 42, "Lucknow": 40, "Hyderabad": 35, "Ahmedabad": 43 }
# Tasks
# 1.
# Display cities having temperature above 40°C.
# 2.
# Find the hottest city.
# 3.
# Find the coolest city.
# 4.
# Calculate average temperature.
# 5.
# Create a list of pleasant cities (temperature < 35°C).
# 6.
# Count cities with temperature between 35°C and 40°C.

# Sample Data
temperature = {
    "Delhi": 41,
    "Mumbai": 33,
    "Chennai": 37,
    "Kolkata": 39,
    "Bengaluru": 28,
    "Pune": 30,
    "Jaipur": 42,
    "Lucknow": 40,
    "Hyderabad": 35,
    "Ahmedabad": 43
}
# Display cities having temperature above 40°C
print("Cities with temperature above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)
print("--------------------------------------------")
# Find the hottest city
hottest_city = ""
max_temp = 0
for city, temp in temperature.items():
    if temp > max_temp:
        max_temp = temp
        hottest_city = city
print("Hottest City:", hottest_city, "(", max_temp, "°C )")
print("--------------------------------------------")
# Find the coolest city
coolest_city = ""
min_temp = float('inf')
for city, temp in temperature.items():
    if temp < min_temp:
        min_temp = temp
        coolest_city = city
print("Coolest City:", coolest_city, "(", min_temp, "°C )")
print("--------------------------------------------")
# Calculate average temperature
total_temp = 0
for temp in temperature.values():
    total_temp += temp
average_temp = total_temp / len(temperature)
print("Average Temperature:", average_temp, "°C")
print("--------------------------------------------")
# Create a list of pleasant cities (temperature < 35°C)
pleasant_cities = []
for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)
print("Pleasant Cities (temperature < 35°C):")
print(pleasant_cities)
print("--------------------------------------------")
# Count cities with temperature between 35°C and 40°C
count = 0
for temp in temperature.values():
    if temp >= 35 and temp <= 40:
        count += 1  
print("Number of cities with temperature between 35°C and 40°C:", count)
print("--------------------------------------------")
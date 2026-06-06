# E-Commerce Order Analysis
# Problem Statement
# An online store records orders as:
# orders = [ ("Laptop", 55000), 
#            ("Mouse", 800), 
#            ("Keyboard", 1500), 
#            ("Monitor", 12000), 
#            ("Pen Drive", 600) ]
# Write a program to:
# • Display all products costing more than ₹1000.
# • Find the most expensive product.
# • Calculate the total order value.
# • Count products costing below ₹1000.

# E-Commerce Order Analysis

orders = [
    ("Laptop", 55000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000),
    ("Pen Drive", 600)
]

# ------------------------------------------------
# Task 1: Display all products costing more than ₹1000

print("Products costing more than ₹1000")

for product in orders:
    if product[1] > 1000:
        print("Product :", product[0])
        print("Price : ₹", product[1])
        print("----------------------")

# ------------------------------------------------
# Task 2: Find the most expensive product

highest_price = orders[0][1]
costly_product = orders[0]

for product in orders:
    if product[1] > highest_price:
        highest_price = product[1]
        costly_product = product

print("Most Expensive Product :", costly_product[0])
print("Price : ₹", highest_price)

print("----------------------")

# ------------------------------------------------
# Task 3: Calculate the total order value

total = 0

for product in orders:
    total += product[1]

print("Total Order Value : ₹", total)

print("----------------------")

# ------------------------------------------------
# Task 4: Count products costing below ₹1000

count = 0

for product in orders:
    if product[1] < 1000:
        count += 1

print("Products below ₹1000 : ", count)
# Sample Data
inventory = {
    "Notebook": 45,
    "Pen": 120,
    "Pencil": 80,
    "Eraser": 25,
    "Marker": 15,
    "Stapler": 8,
    "Glue": 12,
    "Scale": 30,
    "Folder": 5,
    "Calculator": 3
}

# Display products with stock less than 10
print("Products with stock less than 10:")

for product, stock in inventory.items():
    if stock < 10:
        print(product, ":", stock)

# Count products having stock more than 50
count = 0

for stock in inventory.values():
    if stock > 50:
        count += 1

print("\nProducts having stock more than 50:", count)

# Find product with minimum stock
minimum_stock = min(inventory.values())

for product, stock in inventory.items():
    if stock == minimum_stock:
        print("\nProduct with minimum stock:")
        print(product, ":", stock)

# Create list of products that require restocking
restock = []

for product, stock in inventory.items():
    if stock < 20:
        restock.append(product)

print("\nProducts requiring restocking:")
print(restock)

# Calculate total inventory count
total = 0

for stock in inventory.values():
    total += stock

print("\nTotal Inventory Count:", total)
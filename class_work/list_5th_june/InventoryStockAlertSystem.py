# List of stock quantities
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# Count out of stock products
out_of_stock = 0

# List for restock required products
restock = []

# Count available products
available = 0

# List for healthy stock
healthy_stock = []

for i in stock:

    # Out of stock products
    if i == 0:
        out_of_stock += 1

    # Restock required (less than 10)
    if i < 10:
        restock.append(i)

    # Available products
    if i > 0:
        available += 1

    # Healthy stock (>=15)
    if i >= 15:
        healthy_stock.append(i)

# Display output
print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy_stock)
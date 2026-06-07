# Sample Data
prices = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1800,
    "Monitor": 12000,
    "Printer": 9000,
    "Tablet": 28000,
    "Speaker": 3500,
    "Webcam": 2500,
    "Headphones": 4200,
    "Router": 3200
}

# Display products costing more than ₹5000
print("Products costing more than ₹5000:")

for product, price in prices.items():
    if price > 5000:
        print(product, ":", price)

# Count products costing less than ₹3000
count = 0

for price in prices.values():
    if price < 3000:
        count += 1

print("\nProducts costing less than ₹3000:", count)

# Find the most expensive product
highest_price = max(prices.values())

for product, price in prices.items():
    if price == highest_price:
        print("\nMost Expensive Product:")
        print(product, ":", price)

# Create list of products priced between ₹2000 and ₹10000
mid_range = []

for product, price in prices.items():
    if price >= 2000 and price <= 10000:
        mid_range.append(product)

print("\nProducts priced between ₹2000 and ₹10000:")
print(mid_range)

# Calculate total value of all products
total = 0

for price in prices.values():
    total += price

print("\nTotal Value of All Products:", total)
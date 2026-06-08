# Problem Statement
# An e-commerce company stores product sales data as:
# sales = { "Laptop": 15, "Mouse": 45, "Keyboard": 32, "Monitor": 12, "Headphones": 28, "Printer": 8, "Webcam": 20, "Speaker": 18, "Tablet": 10, "Router": 25 }
# Tasks
# 1.
# Display products sold more than 20 times.
# 2.
# Find the best-selling product.
# 3.
# Find the least-selling product.
# 4.
# Calculate total products sold.
# 5.
# Create a list of products requiring promotion (sales < 15).
# 6.
# Count products having sales between 10 and 30.
# Sample Output
# Products Sold More Than 20 Times: Mouse Keyboard Headphones Router Best Selling Product: Mouse (45) Least Selling Product: Printer (8) Total Units Sold: 213 Products Requiring Promotion: ['Monitor', 'Printer', 'Tablet'] Products Having Sales Between 10 and 30: 6



sales = { "Laptop": 15, "Mouse": 45, "Keyboard": 32, "Monitor": 12, "Headphones": 28, "Printer": 8, "Webcam": 20, "Speaker": 18, "Tablet": 10, "Router": 25 }
# Display products sold more than 20 times
print("Products Sold More Than 20 Times:")
for product, quantity in sales.items():
    if quantity > 20:
        print(product)

print("--------------------------------------------")
# Find the best-selling product
# 2. Find the best-selling product

best_product = ""
max_sales = 0

for product, qty in sales.items():
    if qty > max_sales:
        max_sales = qty
        best_product = product

print("Best Selling Product:", best_product, "(", max_sales, ")")
print("--------------------------------------------")
# Find the least-selling product
# Find least-selling product without using min()

least_product = ""
least_sales = float('inf')

for product, qty in sales.items():
    if qty < least_sales:
        least_sales = qty
        least_product = product

print("Least Selling Product:", least_product, "(", least_sales, ")")
print("--------------------------------------------")
# Calculate total products sold
total_sales = 0
for qty in sales.values():
    total_sales += qty
print("Total Units Sold:", total_sales)
print("--------------------------------------------")
# Create a list of products requiring promotion (sales < 15)
promotion_products = []
for product, qty in sales.items():
    if qty < 15:
        promotion_products.append(product)
print("Products Requiring Promotion:", promotion_products)
print("--------------------------------------------")
# Count products having sales between 10 and 30
count = 0
for qty in sales.values():
    if 10 <= qty <= 30:
        count += 1
print("Products Having Sales Between 10 and 30:", count)
print("--------------------------------------------")

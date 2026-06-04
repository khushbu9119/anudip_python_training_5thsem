no_of_item = int(input("Enter the number of items you want to purchase: "))
total_bill = 0
while (no_of_item > 0):
    price = float(input("Enter the price of item: "))
    total_bill += price
    no_of_item -= 1

print("Total bill: $", total_bill)
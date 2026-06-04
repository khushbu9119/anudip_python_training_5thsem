# Program to calculate electricity bill based on units consumed
units = int(input("Enter electricity units consumed: "))

# Initialize bill and category

if units <= 100:
    bill = units * 5                   # Calculate bill for units up to 100
    category = "Low Consumption"

elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)            # Calculate bill for units above 100
    category = "Medium Consumption"

else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)        # Calculate bill for units above 200
    category = "High Consumption"
    
# Display the results
print("Units Consumed:", units)
print("Total Bill: ₹", bill)
print("Category:", category)
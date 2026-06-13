class Product:

    # Constructor
    def __init__(self, name, quantity, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    # Calculate total price
    def calculate_total_price(self):
        return self.quantity * self.price_per_unit

    # Update quantity
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity

    # Display product details
    def display_details(self):
        print("\nProduct Details")
        print("Product Name :", self.name)
        print("Quantity :", self.quantity)
        print("Unit Price : ₹", self.price_per_unit)
        print("Total Price : ₹", self.calculate_total_price())


# Input
name = input("Enter Product Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Unit: ₹"))

# Object Creation
product = Product(name, quantity, price)

# Display Details
product.display_details()

# Update Quantity
new_qty = int(input("\nEnter Updated Quantity: "))
product.update_quantity(new_qty)

print("\nAfter Updating Quantity:")
product.display_details()
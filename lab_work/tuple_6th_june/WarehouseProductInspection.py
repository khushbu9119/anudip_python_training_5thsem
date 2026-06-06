# Problem Statement
# Product IDs and quality status:
# products = [ (101, "Pass"), (102, "Fail"), (103, "Pass"), (104, "Fail"),
# (105, "Pass") ]
# Write a program to:
# • Display failed product IDs.
# • Count passed and failed products.
# • Calculate pass percentage.
# • Stop checking if 3 failures are found.



# Product Quality Analysis

products = [
    (101, "Pass"),
    (102, "Fail"),
    (103, "Pass"),
    (104, "Fail"),
    (105, "Pass")
]

# ------------------------------------------------
# Task 1: Display failed product IDs

print("Failed Product IDs")

for product in products:
    if product[1] == "Fail":
        print(product[0])

print("----------------------")

# ------------------------------------------------
# Task 2: Count passed and failed products

pass_count = 0
fail_count = 0

for product in products:

    if product[1] == "Pass":
        pass_count += 1

    else:
        fail_count += 1

print("Passed Products :", pass_count)
print("Failed Products :", fail_count)

print("----------------------")

# ------------------------------------------------
# Task 3: Calculate pass percentage

pass_percentage = (pass_count / len(products)) * 100

print("Pass Percentage :", pass_percentage, "%")

print("----------------------")

# ------------------------------------------------
# Task 4: Stop checking if 3 failures are found

failures = 0

for product in products:

    if product[1] == "Fail":
        failures += 1

    print(product)

    if failures == 3:
        print("3 failures found. Stopping check.")
        break
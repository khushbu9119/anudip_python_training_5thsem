# Pattern Based Number Printing
rows = int(input("Enter number of rows: "))
# Print the pattern
for i in range(1, rows + 1):    # Loop for each row
    for j in range(1, i + 1):    # Loop for printing numbers in each row
        print(j, end="")        # Print numbers without newline
    print()                     # Move to the next line after each row
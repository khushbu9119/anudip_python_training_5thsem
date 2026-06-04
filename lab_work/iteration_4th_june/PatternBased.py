# Program to print forward and reverse pattern

rows = int(input("Enter number of rows: "))

# Forward Pattern
for i in range(1, rows + 1):         # Loop for each row
    for j in range(1, i + 1):           # Loop for printing numbers in each row
        print(j, end="")                   # Print numbers without newline
    print()                              # Move to the next line after each row

# Reverse Pattern
for i in range(rows, 0, -1):        # Loop for each row in reverse order
    for j in range(1, i + 1):           # Loop for printing numbers in each row
        print(j, end="")            # Print numbers without newline
    print()                        # Move to the next line after each row
# Sample Data
books = {
    "Python Basics": 5,
    "Data Structures": 0,
    "Machine Learning": 3,
    "Java Programming": 2,
    "DBMS": 0,
    "Operating Systems": 6,
    "Networking": 4,
    "Cloud Computing": 1,
    "Cyber Security": 0,
    "Web Development": 7
}

# Display books that are currently unavailable
print("Unavailable Books:")

for book, copies in books.items():
    if copies == 0:
        print(book)

# Count the number of available books
count = 0

for copies in books.values():
    if copies > 0:
        count += 1

print("\nNumber of available books:", count)

# Find the book with maximum copies
max_copies = max(books.values())

for book, copies in books.items():
    if copies == max_copies:
        print("\nBook with maximum copies:")
        print(book, ":", copies)

# Create list of books having less than 3 copies
low_stock = []

for book, copies in books.items():
    if copies < 3:
        low_stock.append(book)

print("\nBooks having less than 3 copies:")
print(low_stock)

# Calculate total number of books available
total = 0

for copies in books.values():
    total += copies

print("\nTotal number of books available:", total)
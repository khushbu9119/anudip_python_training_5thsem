sentence = input("Enter a sentence: ")

count = 0

for ch in sentence:
    if not ch.isalnum() and ch != " ":
        count += 1

print("Number of special characters:", count)
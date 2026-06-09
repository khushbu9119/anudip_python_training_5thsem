# Original text
text = "AAABBBCCCDDDAAA"

# Dictionary for frequency
freq = {}

# Count frequency
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# Display frequencies
print("Character Frequencies:")

for k, v in freq.items():
    print(k, "->", v)

# Unique characters
unique = list(freq.keys())

print("Unique Characters:", unique)

# Find most frequent character
most = max(freq, key=freq.get)

print("Most Frequent Character:", most)

# Compression logic
compressed = ""
count = 1

# Traverse string
for i in range(len(text)-1):

    # If same character
    if text[i] == text[i+1]:
        count += 1

    # If different character
    else:
        compressed += text[i] + str(count)
        count = 1

# Add last character
compressed += text[-1] + str(count)

# Display compressed output
print("Compressed Output:", compressed)

# Length calculations
original_len = len(text)
compressed_len = len(compressed)

# Compression ratio
ratio = (compressed_len / original_len) * 100

print("Original Length:", original_len)
print("Compressed Length:", compressed_len)
print("Compression Ratio:", round(ratio, 2), "%")
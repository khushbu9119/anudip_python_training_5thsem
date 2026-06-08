msg = "Python is awesome and Python is easy to learn"

words = msg.split()

print("Total Characters:", len(msg))
print("Total Words:", len(words))

longest = max(words, key=len)
shortest = min(words, key=len)

print("Longest Word:", longest)
print("Shortest Word:", shortest)

count_python = words.count("Python")
print("Occurrences of Python:", count_python)

more_than_4 = []

for word in words:
    if len(word) > 4:
        more_than_4.append(word)

print("Words Longer Than 4 Characters:", more_than_4)

vowel_words = []

for word in words:
    if word[0].lower() in "aeiou":
        vowel_words.append(word)

print("Words Starting With Vowel:", vowel_words)

vowels = 0
consonants = 0

for ch in msg.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
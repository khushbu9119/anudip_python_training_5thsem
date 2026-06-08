#write a program to find out input the sentence and display the frequency of vowel present in that sentence in that sentence ignoring the case
sentence = input("Enter a sentence: ")

# Convert sentence into lowercase
sentence = sentence.lower()

print("Vowel Frequency:")

if sentence.count('a') > 0:
    print("A =", sentence.count('a'))

if sentence.count('e') > 0:
    print("E =", sentence.count('e'))

if sentence.count('i') > 0:
    print("I =", sentence.count('i'))

if sentence.count('o') > 0:
    print("O =", sentence.count('o'))

if sentence.count('u') > 0:
    print("U =", sentence.count('u'))
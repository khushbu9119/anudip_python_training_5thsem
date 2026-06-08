#Write a program to input a string and input a sentence from user and count the num of character present in it without using len function
sentence = input("Enter a sentence: ")
count = 0
for ch in sentence:
    count += 1

print("Number of characters in the sentence:", count)

print("--------------------------------------------") 

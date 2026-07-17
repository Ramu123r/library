# 12. Write a python program to read a word and print the number of letters, vowels in the word.
word = "Python"

vowels = 0

for ch in word.lower():
    if ch in "aeiou":
        vowels += 1

print("Number of Letters =", len(word))
print("Number of Vowels =", vowels)
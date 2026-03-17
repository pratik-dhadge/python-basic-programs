# Sort letters in a word
word = input("Enter a word: ")
letters = list(word)
letters.sort()
print("Sorted word is:")
for ch in letters:
    print(ch, end="")
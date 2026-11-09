v = ["a","e","i","o","u"]
word = input("Enter a word:")

for letter in  word:
    if letter.lower() in v:
        print(letter)

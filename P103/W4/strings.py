
word = "word"
favorite_letter = input("What is your favorite letter? ")

for index in range(len(word)):
    letter = word[index]
    if letter == favorite_letter:
        print(f"{letter.upper()}")
    else:
        print(f"{letter.lower()}")
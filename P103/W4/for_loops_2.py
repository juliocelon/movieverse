"""
Title: Learning Activity (3 of 3): Looping through Strings

Author: Julio Celón

Use of for loop

"""

favorite_letter = input("What is your favorite letter? ")

word = "Commitment"
for i in range(len(word)):
    if word[i].lower() == favorite_letter.lower():
        #print(word[i].upper(), end="")
        print("_", end="")
    else:
        print(word[i].lower(), end="")
    
"""
Title: W04 Prove: Project Milestone - Word Puzzle

Author: Julio Celón

Milestone Requirements
1. Have a secret word stored in the program.
2. Prompt the user for a guess.
3. Continue looping as long as that guess is not correct.
4. Calculate the number of guesses and display it at the end.

"""

print("\nWelcome to the word guessing game!\n")

secret_word = "pathway"
word_len = len(secret_word)

print("Your hint is: _ _ _ _ _ _ _")

guess = input("\nWhat is your guess? ")
number_try = 1

while guess != secret_word:    
    guess = input("What is your guess? ")
    number_try += 1

print("\nCongratulations! You guessed it!")
print(f"It took you {number_try} guesses.\n")



# Shows creativity and exceeds requirements: I set a limit on the player's guesses and  
#  after each incorrect guess, the player is told how many attempts remain.

"""
Title: Project 04: Word Puzzle

Author: Julio Celón

"""

print("\nWelcome to the word guessing game!\n")

secret_word = "mosiah"
secret_word_len = len(secret_word)

attempts = 1
max_attempts = 5

print(f"\nYou have {max_attempts} attempts to guess the secret word\n")

print("Your hint is: ", end="")
for item in range(secret_word_len):
    print("_ ", end="")
print()

guess = input("\nWhat is your guess? ")

while guess != secret_word and attempts < max_attempts:

    hint_word = ""
    guess_len = len(guess)

    if(guess_len != secret_word_len):
        print("Sorry, the guess must have the same number of letters as the secret word.")
    else:
        for i in range(guess_len):

            if guess[i] == secret_word[i]:
                hint_word = hint_word + guess[i].upper()
            else:
                exists = 0
                for j in range(secret_word_len):

                    if guess[i].lower() == secret_word[j].lower():
                         hint_word = hint_word + guess[i].lower() + " "
                         exists = 1

                if exists == 0:
                    hint_word = hint_word + "_ "
        print(f"hint: {hint_word}")
    
    print(f"You have {max_attempts - attempts} tries left.")
    attempts += 1
    guess = input("\nWhat is your guess? ")


if guess == secret_word:
    print("\nCongratulations! You guessed it!")
    print(f"It took you {attempts} guesses.\n")
else:
    print(f"\nSorry, you've reach the max of tries ({max_attempts})")


"""
Title: Team Activity - Guess My Number Game

Author: Julio Celón

"""

"""
Core Requirement 1
Start by asking the user for the magic number. 
Ask the user for a guess.
Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it.
"""
"""
magic_number = int(input("What is the magic number? "))
guess = int(input("What is your guess? "))

if guess > magic_number:
    print("Lower")
else:
    print("Higher")
"""



"""
Core Requirement 2
Add a loop that keeps looping as long as the guess does not match the magic number.
At this point, the user should be able to keep playing until they get the correct answer.
"""
"""
magic_number = int(input("What is the magic number? "))
guess = int(input("What is your guess? "))
while guess != magic_number:
    if guess > magic_number:
        print("Lower")
    else:
        print("Higher")
    guess = int(input("What is your guess? "))

print("You guessed it!")
"""

# Core Requirement 3
# Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

import random

want_to_play = "yes"

while want_to_play == "yes":

    magic_number = random.randint(1, 10)
    guess = int(input("What is your guess? "))

    number_try = 1 # Stretch Challenge 1

    while guess != magic_number:
        if guess > magic_number:
            print("Lower")
        else:
            print("Higher")
        guess = int(input("What is your guess? "))
        number_try += 1

    print("You guessed it!")
    print(f"Number of tries: {number_try}")

    want_to_play = input("Do you want to play again? ")









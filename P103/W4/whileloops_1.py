"""
Title: Learning Activity (1 of 3): While Loops

Author: Julio Celón

Use a while loop to ask the user for a positive number (>= 0). Continue asking as long as the number is negative, then display the number.

"""


number = float(input("Please type a positive number: "))

while number <= 0 :
    print("Sorry, that is a negative number. Please try again.")
    number = float(input("Please type a positive number: "))

print(f"The number is: {number}")
"""
Title: Learning Activity (1 of 3): While Loops

Author: Julio Celón

Use a while loop, to simulate a child asking their parent for a piece of candy. Have the program keep looping until the user answers "yes", then have the program output "Thank you."

"""

answer = input("May I have a piece of candy? ")

while answer != "yes" :
    answer = input("May I have a piece of candy? ")

print("Thank you")
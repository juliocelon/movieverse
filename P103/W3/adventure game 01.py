"""
Title: Project 03: Adventure Game - Milestone Requirements

Author: Julio Celón

Write a program that determines the letter grade for a course according to the following s

cale:

"""

print("\n - You are in a spacious field, and in the distance, you see a beautiful TREE and a large BUILDING. Where do you go?")
level1 = input("  - Your choice: ")
if level1.upper() == "TREE":
    print("\n - Great! You have chosen the Tree of Life.\n")
elif level1.upper() == "BUILDING":
    print("\n - It's unfortunate, you have chosen the great and spacious building.\n")
else:
    print("\n - You typed an option that doesn't exist, resulting in a loss of the game.\n")

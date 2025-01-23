"""
Author: Julio Celón

Purpose: Demonstrate the basics of reading from a text file in Python.
"""

# IMPORTANT: You should open the folder since this IDE, if not, you wont be able to open the file.
with open("books.txt") as books:
    for line in books:
        print(line.strip())
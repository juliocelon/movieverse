"""
Author: Julio Celón

Title: W06 Team Activity: Human Resource System
"""

# Core Requirement

# IMPORTANT: You should open the folder since this IDE, if not, you wont be able to open the file.

print("\nCore Requirement 1. Open the HR System file, read through it line by line, and at this point, simply display the line to the screen.")
with open("hr_system.txt") as books:
    for line in books:
        print(line)

print("\nCore Requirement 2. Split the line into parts and change your display, so that it shows only the names (instead of the whole line).")
with open("hr_system.txt") as books:
    for line in books:
        new_line = line.split()
        print(f"Name: {new_line [0]}")

print("\nCore Requirement 3. For each line, get the name and the job title for each person, and display those to the screen.")
with open("hr_system.txt") as books:
    for line in books:
        new_line = line.split()
        print(f"Name: {new_line [0]}, Title: {new_line [2]}")

print("\nStretch Challenge 1.")
print("\nStrip off any leading and trailing whitespace from each line.")
print(f"In addition to the name and the job title, also access the salary and the ID number and save them into variables.")
print(f"Display all four values in this format: name (ID: id_number), job_title - $salary. ")
print(f"Don't forget to convert the salary to a number and display it with two decimals.")

with open("hr_system.txt") as books:
    for line in books:
        #line = line.strip()
        new_line = line.strip().split()
        salary = float(new_line[3])
        id_number = new_line[1]
        print(f"{new_line [0]} (ID: {id_number}), {new_line [2]} - ${salary:.2f}")
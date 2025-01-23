"""
Author: Julio Celón

Title: Learning Activity (2 of 2): Data in Files
"""

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

names = []
ages = []

print("\nInstrucion 1. Iterate through the list and display each string to the screen.")
for person in people :
    print(f"{person}")

print("\nInstruction 2. Split the string into a name and age and print them to the screen.")
people_splited = []
for person in people :
    person_splited = person.split()
    people_splited.append(person_splited)
    print(f"{person_splited}")

youngest = 100
name = None
for person_splited in people_splited :
    if int(person_splited[1]) < youngest :
        youngest = int(person_splited[1])
        name = person_splited[0]

print(f"\nInstruction 3 and 4. Find the age that is the youngest and the name of the youngest person: {name}, {youngest} years old")
"""
Author: Julio Celón

Purpose: Display text to the screen.
"""

name="Julio"

complete="Hola + name"

first_name = input("What is your first name?: ")
last_name = input("What is your last name?: ")

output = f"I'm {last_name.title()}, {first_name.title()} {last_name.title()}"
print(output)

print("----")

color = input('What is your favorite color?: ')
print('Your favorite color is ' + color )
# Shows creativity and exceeds requirements: I introduced a welcome message at the start of the program and added a prompt for the user to input 
# three additional words: emotion, location, and name. These words are then incorporated into two additional lines at the end of the story.

"""
Title: Project 01: Clever Stories

Author: Julio Celón

"""

print("\nWelcome! Let's play Mad Libs!!")

print("\nPlease enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb_1 = input("verb: ")
exclamation = input("exclamation: ")
verb_2 = input("verb: ")
verb_3 = input("verb: ")

# additional words required
emotion = input("emotion: ")
location = input("location: ")
name = input("name: ")

print("\nYour story is:\n")
print("----------------------------------------\n")

print("The other day, I was really in trouble. It all started when I saw a very")
print(f'{adjective} {animal} {verb_1} down the hallway. \n"{exclamation.capitalize()}!" I yelled. But all')
print(f"I could think to do was to {verb_2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb_3}")
print("right in front of my family.")

# Two additional lines to extend the story
print(f"Everyone was {emotion}, my friend {name.capitalize()} was there too, and we couldn't believe what we had just witnessed.")
print(f"After that, we all stayed in the {location} to avoid any more surprises.")
print("\n----------------------------------------\n")




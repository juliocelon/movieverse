"""
Author: Julio Celón

Purpose: Practice using lists, by adding the names of friends.
"""

friends = []

answer = None
while answer != "end":

    answer = input("Type the name of a friend: ")
    if answer != "end":
        friends.append(answer)

print("\nYour friends are:")
for friend in friends:
    print(friend)


"""
Author: Julio Celón

Purpose: Practice using lists, by adding the names of friends.
"""

shooping_list = []

item = None
print("Please enter the item of the shopping list (type: quit to finish):")
while item != "quit":

    item = input("Item: ")
    if item != "quit":
        shooping_list.append(item)

print("\nThe shopping list is:")
for item in shooping_list:
    print(item)

print("The shopping list with indexes is:")
for i in range(len(shooping_list)):
    print(f"{i}. {shooping_list[i]}")

index_change = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shooping_list[index_change] = new_item

print("The shopping list with indexes is:")
for i in range(len(shooping_list)):
    print(f"{i}. {shooping_list[i]}")

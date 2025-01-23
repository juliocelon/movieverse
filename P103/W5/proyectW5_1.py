""""
Author: Julio Celón
W05 Prove: Milestone Requirements

1. Have menu system that repeats until the user chooses quit.
2. Create a list that will store the names of the items in the shopping cart.
3. Complete the option to add the name of the item to the list.
4. Complete the option to display the names of the items in the list.

"""

print("\nWelcome to the Shopping Cart Program!")

items = []
answer = None

while answer != 5 :

    print("\nPlease select one of the following:\n") 
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    answer = int(input("\nPlease enter an action: "))

    if answer == 1 :

        item = input("\nWhat item would you like to add? : ")
        items.append(item)
        print(f"\n'{item}' has been added to the cart.")

    elif answer == 2 : 

        print("\nThe contents of the shopping cart are:\n")
        for i in range(len(items)) :
            print(f"{items[i]}")

print("\nThank you. Goodbye.\n")
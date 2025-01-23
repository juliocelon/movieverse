# Shows creativity and exceeds requirements: I aligned items with prices and display a message 
#    if the cart is emptyin 'View Cart', 'Remove item' and 'Compute total', and added the item count in 'Compute total'.
""""
Author: Julio Celón
W05 Prove: Project - Shopping Cart
"""

print("\nWelcome to the Shopping Cart Program!")

items = []
prices = []
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
        price = float(input(f"What is the price of '{item}'? : "))
        items.append(item)
        prices.append(price)
        print(f"\n'{item}' has been added to the cart.")

    elif answer == 2 : 

        if len(items) == 0 :
            print("\nThe shopping cart is empty")
        else:
            print("\nThe contents of the shopping cart are:\n")
            print(f"{'#  '}{'Item':<9}{'Price':>9}")
            for i in range(len(items)) :
                print(f"{i+1}. {items[i]:<9} ${prices[i]:>9.2f}")

    elif answer == 3 :

        if len(items) == 0 :
            print("\nThe shopping cart is empty")
        else:
            print("\nThe contents of the shopping cart are:\n")
            print(f"{'#  '}{'Item':<9}{'Price':>9}")
            for i in range(len(items)) :
                print(f"{i+1}. {items[i]:<9} ${prices[i]:>9.2f}")

            item_remove = int(input("\nWhich item would you like to remove? "))
            items.pop(item_remove-1)
            prices.pop(item_remove-1)
            print("\nItem removed")

    elif answer == 4 :

        if len(items) == 0 :
            print("\nThe shopping cart is empty")
        else:
            sum = 0
            for price in prices :
                sum += price
            print(f"\nThe total price of the {len(items)} items in the shopping cart is ${sum:.2f}")

print("\nThank you. Goodbye.\n")
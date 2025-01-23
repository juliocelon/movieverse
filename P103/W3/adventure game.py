# Shows creativity and exceeds requirements: I introduced a welcome and explanation message at the start of the program 
# and added in two different situations an extra level (level 4) 

"""
Title: Project 03: Adventure Game

Author: Julio Celón

Write a program that determines the letter grade for a course according to the following scale:

"""

print("\nWelcome to your Adventure Game")
print("\n  If you type an incorrect option, you will lose the game")

print("\n - You are in a spacious field, and in the distance, you see a beautiful TREE and a large BUILDING. Where do you go?")
level1 = input("  - Your choice: ")

if level1.upper() == "TREE":
    print("\n - On your way to the tree, a mist of darkness begins to appear, but you notice there is an IRON rod and a SILK thread. Which do you choose?")
    level2 = input("  - Your choice: ")

    if level2.upper() == "IRON" :
        print("\n - Finally, you reach the tree. You can EAT its fruit, CALL your family, or GO somewhere else. What do you choose?")
        level3 = input("  - Your choice: ")

        if level3.upper() == "EAT":
            print("\n - Congratulations!, you have eaten from the Tree of Life!")

        elif level3.upper() == "CALL":
            print("\n - You manage to find your family, and they come toward you. You can EAT its fruit or GO somewhere else. What do you choose?")
            level4 = input("  - Your choice: ")

            if level4.upper() == "EAT":
                print("\n - Congratulations!, you and your family have eaten from the Tree of Life!")

            elif level4.upper() == "GO":
                print("\n - Because you decide to go somewhere else, you as a family become separated and lost in the darkness.")

            else:
                print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

        elif level3.upper() == "GO":
            print("\n - Because you decide to go somewhere else, you get lost in the darkness.")
        
        else:
            print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

    elif level2.upper() == "SILK" :
        print("\n - This silk thread is extremely thin, making it difficult to continue using as a guide. You can either LEAVE it behind or KEEP following it.")
        level3 = input("  - Your choice: ")

        if level3.upper() == "LEAVE":
            print("\n - Now you're on your own, but you fall into a deep cave from which you can't escape.")

        elif level3.upper() == "KEEP":
            print("\n - As you continue, you realize that you end up trapped in a spider web.")

        else:
            print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")
    else:
        print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

elif level1.upper() == "BUILDING":
    print("\n - On your way to the building, a mist of darkness begins to appear, but you notice that there is a RIVER or a FOREST nearby. Which do you choose?")
    level2 = input("  - Your choice: ")

    if level2.upper() == "RIVER" :
        print("\n - To cross the river, you can SWIM or TAKE a boat. Which do you choose?")
        level3 = input("  - Your choice: ")

        if level3.upper() == "SWIM":
            print("\n - The river has a strong current, so you are unable to make it across and drown.")

        elif level3.upper() == "TAKE":
            print("\n - With the boat, you successfully cross the river and arrive at the building.")
            print("\n - You see people in the tree; you can either LAUGH at them or GO to the tree. What will you do?")
            level4 = input("  - Your choice: ")

            if level4.upper() == "LAUGH":
                print("\n - You stay in the building, but it collapses, and you don't survive.")

            elif level4.upper() == "GO":
                print("\n - Congratulations! Through your repentance, you are able to reach the tree and partake of its fruit.")

            else:
                print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

        else:
            print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

    elif level2.upper() == "FOREST":
        print("\n - In the forest, you see two animals that you can choose to follow: a RABBIT and a SNAKE. Which one do you follow?")
        level3 = input("  - Your choice: ")

        if level3.upper() == "RABBIT":
            print("\n - The rabbit leads you to its hiding place, where upon entering, you emerge from your dream safe and sound.")

        elif level3.upper() == "SNAKE":
            print("\n - The snake leads you to its hiding place, where upon entering, it bites you, and you are poisoned.")

        else:
            print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

    else:
        print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

else:
    print("\n - You typed an option that doesn't exist, resulting in a loss of the game.")

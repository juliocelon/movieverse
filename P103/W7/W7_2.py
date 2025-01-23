""""
Author: Julio Celón

W07 - Learning Activity (2 of 2): Function Practice
"""

def compute_area_square(square_length):
    return square_length ** 2

def compute_area_rectangle(rectangle_length, rectangle_width):
    return rectangle_length * rectangle_width

def compute_area_circle(circle_radius):
    return 3.1416 * circle_radius ** 2 

option = None

while option != "quit":
    print("\nWhat kind of shape do you have? \n")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("\nType 'quit' to exit\n")
    option = input("Your choice: ")

    if option == "1":
        side = float(input("\nWhat is the length of a side of the square? "))
        area_square = compute_area_rectangle(side, side)
        print(f"\nThe area of the square is: {area_square:.2f}")

    elif option == "2":
        length = float(input("\nWhat is the length of rectangle? "))
        width = float(input("What is the width of the rectangle? "))
        area_rectangle = compute_area_rectangle(length, width)
        print(f"\nThe area of the rectangle is: {area_rectangle:.2f}")

    elif option == "3":
        radius = float(input("\nWhat is the radius of the circle? "))
        area_circle = compute_area_circle(radius)
        print(f"\nThe area of the circle is: {area_circle:.2f}")
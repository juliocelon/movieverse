"""
Title: Team Activity - Areas of Shapes

Author: Julio Celón

"""
import math

square_length = float(input("\nWhat is the length of a side of the square? "))
print(f"The area of the square is: {( square_length ** 2 ):.2f}")

rectangle_length = float(input("\nWhat is the length of rectangle? "))
rectangle_width = float(input("What is the width of the rectangle? "))
print(f"The area of the rectangle is: {(rectangle_length * rectangle_width):.2f}")

circle_radius = float(input("\nWhat is the radius of the circle? "))
print(f"The area of the circle is: {(3.1416 * circle_radius ** 2 ):.2f}")

# Stretch Challenge 1
circle_radius = float(input("\nWhat is the radius of the circle? "))
print(f"The area of the circle is: {(math.pi * circle_radius ** 2 ):.2f}")

# Stretch Challenge 2
print(f"\nWith your new single value, we will get the areas of a square, circle and volumes of a cube and sphere")
single_value = float(input("\nWhat is the single value?: "))

print(f"The area of the square is: {( single_value * single_value ):.2f}")
print(f"The area of the circle is: {( math.pi * single_value ** 2 ):.2f}")
print(f"The volume of the cube is: {( single_value ** 3 ):.2f}")
print(f"The volume of the sphere is: {((4/3) * math.pi * single_value ** 3 ):.2f}")

# Stretch Challenge 3
square_lengt_cm = float(input("\nWhat is the length of a side of the square (in centimeters)? "))
print(f"The area of the square in centimeters is: {( square_lengt_cm ** 2 ):.2f} cm²")
print(f"The area of the square in meters is: {( (square_lengt_cm ** 2) / 10000 ):.5f} m²")

rectangle_length_cm = float(input("\nWhat is the length of rectangle (in centimeters)? "))
rectangle_width_cm = float(input("What is the width of the rectangle (in centimeters)? "))
print(f"The area of the rectangle in centimeters is: {( rectangle_length_cm * rectangle_width_cm ):.2f} cm²")
print(f"The area of the rectangle in meters is: {( ( rectangle_length_cm * rectangle_width_cm ) / 10000 ):.5f} m²")

circle_radius_cm = float(input("\nWhat is the radius of the circle (in centimeters) ? "))
print(f"The area of the circle in centimeters is:: {(math.pi * circle_radius_cm ** 2 ):.2f} cm²")
print(f"The area of the circle in meters is: {((math.pi * circle_radius_cm ** 2 ) / 10000 ):.5f} m²")








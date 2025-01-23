"""
Title: Project 02: Meal Price Calculator - Milestone Requirements

Author: Julio Celón

"""

childs_meal_price = float(input("What is the price of a child's meal? "))
adults_meal_price = float(input("What is the price of a adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))

meals_subtotal = number_children * childs_meal_price + number_adults * adults_meal_price
print(f"\nSubtotal : ${meals_subtotal:.2f}")



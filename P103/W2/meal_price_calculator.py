# Shows creativity and exceeds requirements: I introduced a welcome message at the start of the program 
# and added at the end of the program a Next Visit Discount which is based on your total payment amount.

"""
Title: Project 02: Meal Price Calculator - Final requirements

Author: Julio Celón

"""

print("\nWelcome to your new Meal Price Calculator")
print("\nPlease enter the following:\n")

childs_meal_price = float(input("What is the price of a child's meal? "))
adults_meal_price = float(input("What is the price of a adult's meal? "))
number_children = int(input("How many children are there? "))
number_adults = int(input("How many adults are there? "))

meals_subtotal = number_children * childs_meal_price + number_adults * adults_meal_price
print(f"\nSubtotal : ${meals_subtotal:.2f}")

sales_tax_percentage = float(input("\nWhat is the sales tax rate? "))
sales_tax = meals_subtotal * sales_tax_percentage / 100
print(f"Sales Tax: ${sales_tax:.2f}")

total = meals_subtotal + sales_tax
print(f"Total: ${total:.2f}")

payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total
print(f"Change: ${change:.2f}")

print("\nThe Next Visit Discount is based on your total payment amount.")
discount_rate = float(input("What is the discount rate for the next visit? "))
next_visit_discount = total * discount_rate / 100
print("\n--------------------------------------")
print("* SPECIAL TICKET *")
print(f"Next Visit Discount: ${next_visit_discount:.2f}")
print("Save this for your next visit!")
print("--------------------------------------")



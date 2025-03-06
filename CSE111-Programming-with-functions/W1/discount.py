"""
Work as a team to write a Python program named discount.py that gets a customer’s subtotal as input 
and gets the current day of the week from your computer’s operating system. 

Your program must not ask the user to enter the day of the week. 
Instead, it must get the day of the week from your computer’s operating system.

If the subtotal is $50 or greater and today is Tuesday or Wednesday, your program must subtract 10% from the subtotal. 
Your program must then compute the total amount due by adding sales tax of 6% to the subtotal. 
Your program must print the discount amount if applicable, the sales tax amount, and the total amount due.
"""

from datetime import datetime

day_of_week = datetime.now().weekday()
# 0 is monday , 1 is tuesday, 2 is wednesday, ...

subtotal = float(input("Please enter the subtotal: "))

if ( day_of_week == 1 or day_of_week == 2 ) and subtotal >= 50 :
     subtotal -= subtotal*0.1

tax_amount = subtotal * 0.06
print(f"Sales tax amount: {tax_amount:.2f}")

print(f"Total: {subtotal+tax_amount:.2f}")


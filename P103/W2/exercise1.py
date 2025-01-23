"""
Learning Activity (1 of 2): Numeric Variables

Author: Julio Celón
"""

age = int(input("How old are you? "))
print(f"On your next birthday, you will be {str(age+1)}\n")

cartons = int(input("How many egg cartons do you have? "))
print(f"You have {str(cartons*12)} eggs\n")

cookies = float(input("How many cookies do you have? "))
people = float(input("How many people are there? "))
print(f"Each person may have {str(cookies/people)} cookies\n")

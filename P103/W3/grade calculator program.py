"""
Title: Team Activity - Grade Calculator Program

Author: Julio Celón

Write a program that determines the letter grade for a course according to the following scale:

A >= 90
B >= 80
C >= 70
D >= 60
F < 60

"""

# Core Requirement 1 & 2
grade = int(input("Please, input the grade percentage: "))
letter = ""

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

# Stretch Challenge 1
reminder = grade % 10
sign = ""
if reminder >= 7 :
    sign = "+"
elif reminder < 3 :
    sign = "-"

# Stretch Challenge 2
if letter == "A" :
    if sign == "+":
        sign = ""

# Stretch Challenge 3
if letter == "F" :
    sign = ""

print(f"Grade:{letter}{sign}")

# Core Requirement 2
if grade >= 70:
    print("Congratulations on passing the course! Your hard work and dedication have paid off, and you should be proud of this achievement. Keep up the great work!")
else:
    print("Unfortunately, you didn't pass the course this time. But don't get discouraged! Every challenge is a learning opportunity, and with a bit more effort and practice, you can succeed next time. Keep going—you’ve got this!")




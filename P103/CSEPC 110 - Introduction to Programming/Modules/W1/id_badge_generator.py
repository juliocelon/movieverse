"""
Title: Individual Activity: ID Badge Generator

Author: Julio Celón

"""

print("\nPlease enter the following information:")

first_name = input("First name: ")
last_name = input("Last name: ")
email = input("Email address: ")
phone_number = input("Phone number: ")
job_title = input("Job title: ")
id_number = input("ID number: ")
hair_color = input("Hair color: ")
eye_color = input("Eye color: ")
month_started = input("Month you started: ")
advanced_training_completed = input("Advanced training completed?: ")

print("\nThe ID Card is:\n----------------------------------------")
print(f"{last_name.upper()}, {first_name}")
print(f"{job_title.capitalize()}")
print(f"ID: {id_number}\n")
print(f"{email.lower()}")
print(f"{phone_number}\n")

print(f"Hair: {hair_color:<15}\tEyes: {eye_color}")
print(f"Month: {month_started:<15}\tTraining: {advanced_training_completed}")

"""
# There are various ways to accomplish the spacing

# In this approach, I told it that hair_color will take exactly 15
# spaces, and month will take 14. That way, the next columns will
# line up. I had to do month 14 (instead of 15) because the word
# 'Month' that came before my value was one letter longer.

print(f"Hair: {hair_color:15} Eyes: {eye_color}")
print(f"Month: {month:14} Training: {training}")
"""

print("----------------------------------------")







"""
Author: Julio Celón
Title: W01 Prove Assignment: Tire Volume

Assignment

Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and 
computes and outputs the volume of space inside that tire.

"""
import math
from datetime import datetime

width_tire_mmm = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_inches = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width_tire_mmm**2 * aspect_ratio * (width_tire_mmm * aspect_ratio + (2540 * diameter_inches))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")

current_date_and_time = datetime.now()

"""
Exceeding the Requirements
2. After your program prints the tire volume to the terminal window, your program should ask the user if 
    she wants to buy tires with the dimensions that she entered. If the user answers “yes”, your program 
    should ask for her phone number and store her phone number in the volumes.txt file.
"""
phone_number=""
buy_tires = input("Do you want to buy the tires? (y/n): ")

if(buy_tires == "y"):
    phone_number = input("provide phone number: ")
    with open("volumes.txt", mode="at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width_tire_mmm}, {aspect_ratio}, {diameter_inches}, {volume:.2f}, {phone_number}", file=volumes_file)
else:
    with open("volumes.txt", mode="at") as volumes_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {width_tire_mmm}, {aspect_ratio}, {diameter_inches}, {volume:.2f}", file=volumes_file)


"""
Exceeding the Requirements
   1. Find tire prices for four or more tire sizes online. 
      Add a set of if … elif … else statements in your program that use the tire width, tire aspect ratio, 
      and wheel diameter that the user enters to find a price and then print the price.
"""
# Prices for specific tire sizes
if width_tire_mmm == 225 and aspect_ratio == 45 and diameter_inches == 17:
    price = "$ 1,759" 
elif width_tire_mmm == 205 and aspect_ratio == 55 and diameter_inches == 16:
    price = "$ 1,129"
elif width_tire_mmm == 195 and aspect_ratio == 65 and diameter_inches == 15:
    price = "$ 1,099"  
elif width_tire_mmm == 185 and aspect_ratio == 60 and diameter_inches == 15:
    price = "$ 1,039"
else:
    price = "not available" 

print(f"The price of the tire {width_tire_mmm}/{aspect_ratio}R{diameter_inches} is {price}")

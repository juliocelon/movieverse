"""
Author: Julio Celón
Title: W01 Project Milestone: Tire Volume

Assignment

Write a Python program named tire_volume.py that reads from the keyboard the three numbers for a tire and 
computes and outputs the volume of space inside that tire.

"""
import math

width_tire_mmm = float(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter_inches = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width_tire_mmm**2 * aspect_ratio * (width_tire_mmm * aspect_ratio + (2540 * diameter_inches))) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")
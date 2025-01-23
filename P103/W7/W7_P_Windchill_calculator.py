# Shows creativity and exceeds requirements: I added a title in the beginning of the program, and implemented a loop using a while statement to allow the user 
#  to continue generating wild chill values as needed.

"""
Author: Julio Celón

Title: Project 07: Windchill Calculator

Assignment
Your assignment is to write a program that asks the user for a temperature and then shows the wind chill values for various wind speeds at that temperature.

Your program should compute and display the wind chill for wind speeds of 5, 10, 15, ..., 60 miles per hour, just like the National Weather Service chart does.
To help users who are more familiar with Celsius, your program should allow temperature to be entered in either Celsius or Fahrenheit, and if needed, 
convert the Celsius temperature to Fahrenheit before using the formula.

"""

def get_wind_chill(air_temperature, wind_speed):
    wind_chill = 35.74 + (0.6215 * air_temperature) - (35.75 * wind_speed ** 0.16) + (0.4275 * air_temperature * wind_speed ** 0.16)
    return wind_chill

print("\nWindchill Calculator")

option = "Y"
while option.upper() == "Y":
    
    air_temperature = float(input("\nWhat is the temperature? "))
    scale = input("Fahrenheit or Celsius (F/C)? ")
    print()

    if scale.upper() == "C" :
        air_temperature = 9/5 * air_temperature + 32

    for wind_speed in range(5 ,65, 5):
        print(f"At temperature {air_temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {get_wind_chill(air_temperature, float(wind_speed)):.2f}F")

    option = input("\nDo you want to get the wild chill values for another temperature? (Y/N): ")
    print()
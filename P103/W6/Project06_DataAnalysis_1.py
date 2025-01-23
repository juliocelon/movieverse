"""
Author: Julio Celón

Title: Project 06: Data Analysis - Milestone Requirements

1. Download the dataset
2. Load the dataset in your Python program
3. Iterate through the data line by line
4. Split each line into parts
5. Find the lowest value for life expectancy and the highest value for life expectancy in the dataset, 
        and display both values. (Note that at this point, you just need the value for this, 
        not the year and the country for that value.)

"""

lowest_life_expectancy = 120
highest_life_expectancy = 0

with open("life-expectancy.csv") as data:
    line_zero = 0

    for line in data:
        if line_zero != 0:
            splitted_line = line.strip().split(",")

            life_expectancy = float(splitted_line[3])

            if life_expectancy < lowest_life_expectancy:
                lowest_life_expectancy = life_expectancy

            if life_expectancy > highest_life_expectancy:
                highest_life_expectancy = life_expectancy
            
        line_zero += 1

    print(f"The overall min life expectancy is: {lowest_life_expectancy}")
    print(f"The overall max life expectancy is: {highest_life_expectancy}")
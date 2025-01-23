# Shows creativity and exceeds requirements: I added a feature that lets the user input a country to display its minimum, maximum, and average life expectancy. 
#   The input and file data are matched in lowercase, and if the country isn't found, the user is notified.

"""
Author: Julio Celón

Title: Project 06: Data Analysis

Assignment
Download the dataset and write a Python program to analyze it to answer the following questions:

1. What is the year and country that has the lowest life expectancy in the dataset?
2. What is the year and country that has the highest life expectancy in the dataset?
3. Allow the user to type in a year, then, find the average life expectancy for that year. 
    Then find the country with the minimum and the one with the maximum life expectancies for that year.

"""

year_of_interest = input("\nEnter the year of interest: ")
year_counter = 0
year_sum = 0
min_year_country = None
max_year_country = None
min_year_life_expectancy = 120
max_year_life_expectancy = 0

min_life_expectancy = 120
max_life_expectancy = 0

min_life_expectancy_country  = None
min_life_expectancy_year = None

max_life_expectancy_country  = None
max_life_expectancy_year = None

with open("life-expectancy.csv") as data:
    line_zero = 0

    for line in data:
        if line_zero != 0:
            splitted_line = line.strip().split(",")

            life_expectancy = float(splitted_line[3])
            country = splitted_line[0]
            year = splitted_line[2]

            if life_expectancy < min_life_expectancy:
                min_life_expectancy = life_expectancy
                min_life_expectancy_country = country
                min_life_expectancy_year = year

            if life_expectancy > max_life_expectancy:
                max_life_expectancy = life_expectancy
                max_life_expectancy_country = country
                max_life_expectancy_year = year

            if year_of_interest == year:
                year_counter += 1
                year_sum += float(life_expectancy)

                if life_expectancy < min_year_life_expectancy:
                    min_year_life_expectancy = life_expectancy
                    min_year_country = country

                if life_expectancy > max_year_life_expectancy:
                    max_year_life_expectancy = life_expectancy
                    max_year_country = country

        line_zero += 1

print(f"\nThe overall max life expectancy is: {max_life_expectancy} from {max_life_expectancy_country} in {max_life_expectancy_year}")
print(f"The overall min life expectancy is: {min_life_expectancy} from {min_life_expectancy_country} in {min_life_expectancy_year}")

print(f"\nFor the year {year_of_interest}:")

avg_life_expectancy = year_sum / year_counter
print(f"The average life expectancy across all countries was {avg_life_expectancy:.2f}")

print(f"The max life expectancy was in {max_year_country} with {max_year_life_expectancy}")
print(f"The min life expectancy was in {min_year_country} with {min_year_life_expectancy}\n")



# Showing Creativity and Exceeding Requirements:

country_of_interest = input("\nEnter the country of interest: ")

min_life_expectancy = 120
max_life_expectancy = 0

min_life_expectancy_country  = None
min_life_expectancy_year = None

max_life_expectancy_country  = None
max_life_expectancy_year = None

year_counter = 0
year_sum = 0

with open("life-expectancy.csv") as data:
    line_zero = 0

    for line in data:
        if line_zero != 0:
            splitted_line = line.strip().split(",")

            country = splitted_line[0]
            year = splitted_line[2]
            life_expectancy = float(splitted_line[3])

            if country.lower() == country_of_interest.lower():
                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy
                    min_life_expectancy_year = year

                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy
                    max_life_expectancy_year = year

                year_counter += 1
                year_sum += float(life_expectancy)

        line_zero += 1

if year_counter > 0:
    print(f"The overall max life expectancy is: {max_life_expectancy} from {country_of_interest} in {max_life_expectancy_year}")
    print(f"The overall min life expectancy is: {min_life_expectancy} from {country_of_interest} in {min_life_expectancy_year}")

    avg_life_expectancy = year_sum / year_counter
    print(f"The average life expectancy from {country_of_interest} is {avg_life_expectancy:.2f}")
else:
    print(f"\nThe country you typed does not exist in our data: {country_of_interest}\n")
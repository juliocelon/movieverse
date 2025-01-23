"""
Author: Julio Celón

Team Activity - Lists of Numbers
"""

"""
numbers = []

number = None
print("Enter a list of numbers, type 0 when finished.")

while number != 0:

    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0
max = 0
print("\nNumbers:")
for number in numbers:
    sum += number
    if number > max:
        max = number

    print(number)

average = sum/len(numbers)

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {max}")
"""

#Stretch Challenge 
"""
1. Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).
2. Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.
"""

numbers = []
number = None
print("Enter a list of numbers, type 0 when finished.")

while number != 0:
    number = int(input("Enter number: "))
    if number != 0:
        numbers.append(number)

sum = 0
max = 0
min = 100
print("\nNumbers:")
for number in numbers:
    sum += number

    if number > max:
        max = number
    
    ## Stretch Challenge 1
    if number < min and number > 0: 
        min = number

average = sum/len(numbers)

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {max}")
print(f"The smallest positive number is: {min}")

## Stretch Challenge 2
print("The sorted list is:")
numbers.sort()
for number in numbers:
    print(number)

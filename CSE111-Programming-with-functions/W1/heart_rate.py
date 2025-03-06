"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = float(input("Please enter your age:"))

maximum_rate = 220 - age
min_range = maximum_rate * (65/100)
max_range = maximum_rate * (85/100)

print("When you exercise to strengthen your heart, you should")
print(f"keep your heart rate between {int(min_range)} and {int(max_range)} beats per minute.")
"""
Author: Dua Hasan
Date: February 5, 2025
File Name: hasan_lemonadeStandSchedule.py
Description: This program manages a weekly schedule for a lemonade stand.
"""

# Defining the list of tasks related to running a lemonade stand
tasks = ["Buy lemons", "Make lemonade", "Sell lemonade", "Count earnings", "Clean up"]

# Using a for loop to iterate over the list of tasks and print them to the console
print("Lemonade Stand Tasks for the Week:")
for task in tasks:
    print(task)

# Defining a list of days of the week
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Using a for loop to iterate over the list of days and associate each with a task
print("\nLemonade Stand Schedule:")
for i, day in enumerate(days_of_week):
    if day == "Saturday" or day == "Sunday":
        print(f"{day}: It's a day off! Rest up and enjoy!")
    else:
        print(f"{day}: Task - {tasks[i]}")


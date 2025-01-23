"""
Author: Dua Hasan
Date: 01/22/2025
File Name: hasan_lemonadeStand.py
Description: This program simulates a lemonade stand by calculating the cost of making lemonade
and the profit from selling it.
"""

# Function to calculate the cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    """
    This function calculates the total cost of making lemonade by adding the cost of lemons
    and sugar.
    """
    total_cost = lemons_cost + sugar_cost  # Adding cost of lemons and sugar
    return total_cost  # Returning the total cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    This function calculates the profit by subtracting the total cost from the selling price.
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost)  # Getting the total cost
    profit = selling_price - total_cost  # Calculating the profit
    return profit  # Returning the profit

# Variables to test the functions
lemons_cost = 3  # Cost of lemons
sugar_cost = 2   # Cost of sugar
selling_price = 10  # Selling price of lemonade

# Build the result strings
cost_result = str(lemons_cost) + " + " + str(sugar_cost) + " = " + str(calculate_cost(lemons_cost, sugar_cost))  # Cost calculation
profit_result = "Profit: " + str(calculate_profit(lemons_cost, sugar_cost, selling_price))  # Profit calculation

# Output the results to the console
print("Cost Calculation: " + cost_result)  # Printing cost calculation
print(profit_result)  # Printing profit calculation

# Day 2: Operators
# Task
# Given the meal price (base cost of a meal),
# tip percent (the percentage of the meal price being added as tip),
# and tax percent (the percentage of the meal price being added as tax) for a meal,
# find and print the meal's total cost.
# Round the result to the nearest integer.

import sys

# Complete the solve function below.

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    tip_amount= (tip_percent/100) * meal_cost
    tax_amount= (tax_percent/100) * meal_cost
    
    total_cost= round(meal_cost+tip_amount+tax_amount)
    print(total_cost) 

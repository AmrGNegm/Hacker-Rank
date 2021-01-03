#Day 1: Standard Deviation

# Given an array, X,n of  integers, calculate and print the standard deviation.
#Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3 format).
#An error margin of ±1 will be tolerated for the standard deviation.



# Import library
import math

# Define functionts
def mean(data):
    return sum(data) / len(data)

def stddev(data, size):
    sum = 0
    for i in range(size):
        sum = sum + (data[i] - mean(data)) ** 2
    return math.sqrt(sum / size)

# Set data
size = int(input())
numbers = list(map(int, input().split()))

# Get standard deviation
print(round(stddev(numbers, size), 1))

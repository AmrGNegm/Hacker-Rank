# Day 1: Quartiles
# Given an array, X of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3).
#It is guaranteed that Q1, Q2, and Q3 are integers.



# Enter your code here. Read input from STDIN. Print output to STDOUT
# Define functions
def median(size, values):
    if size % 2 == 0:
        median = (values[int(size/2)-1] + values[int(size/2)]) / 2
    else:
        median = values[int(size/2)]
    return int(median)

# Set the data
size = int(input())
numbers = sorted(list(map(int, input().split())))

# Verify that the total data is even or odd
if size % 2 == 0:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):size]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:size]

# Get the final result and print on the screen
print (median(len(data_low), data_low))
print (median(size, numbers))
print (median(len(data_high), data_high))

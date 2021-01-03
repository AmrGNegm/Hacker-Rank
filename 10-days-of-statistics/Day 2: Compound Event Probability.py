# Day 2: Compound Event Probability

# Task
# There are 3 urns labeled X, Y, Z and .


# X Urn  contains 4 red balls and 3 black balls.
# Y Urn  contains 5 red balls and 4 black balls.
# Z Urn  contains 4 red balls and 4 black balls.

# One ball is drawn from each of the 3 urns.
# What is the probability that, of the 3 balls drawn, 2 are red and 1 is black?

# Set data
x = {"Red":4/7, "Black":3/7}
y = {"Red":5/9, "Black":4/9}
z = {"Red":4/8, "Black":4/8}

# Get possibilities
first_possibility = x["Red"] * y["Red"] * z["Black"]
second_possibility = x["Red"] * y["Black"] * z["Red"]
third_possibility = x["Black"] * y["Red"] * z["Red"]

# Get probability
print(first_possibility + second_possibility + third_possibility)

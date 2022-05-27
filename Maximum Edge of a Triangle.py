# Maximum Edge of a Triangle
# Create a function that finds the maximum range of a triangle's third edge,
# where the side lengths are all integers.
# Examples:
# max_edge(8, 10) ➞ 17
# max_edge(5, 7) ➞ 11
# max_edge(9, 2) ➞ 10
# Difficulty: very easy
# Date: 8/7/2021

number1 = int(input("Enter a triangle edge length: "))
number2 = int(input("Enter another length: "))

def max_edge(number1, number2):
    maximum_edge = number1 + number2 - 1
    return maximum_edge

print("The maximum edge of this triangle is: "+str(max_edge(number1,number2)))


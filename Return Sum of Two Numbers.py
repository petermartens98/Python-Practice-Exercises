# Return the Sum of Two Numbers
# Create a function that takes two numbers as arguments and return their sum.
# Difficulty: Very Easy
# Date: 8/5/2021

import math

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))


def addition(number1,number2):
    sum = number1 + number2
    return sum


print("their sum is: "+str(addition(number1,number2)))


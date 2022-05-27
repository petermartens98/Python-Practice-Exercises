# Quadratic Equation
# Create a function to find only the root value of x in any quadratic equation ax^2 + bx + c.
# The function will take three arguments:
#   a as the coefficient of x^2
#   b as the coefficient of x
#   c as the constant term
# Examples:
#   quadratic_equation(1, 2, -3) ➞ 1
#   quadratic_equation(2, -7, 3) ➞ 3
#   quadratic_equation(1, -12, -28) ➞ 14
# Notes:
#   Quadratic equation is always guaranteed to have a root.
#   Calculate only the root that sums the square root of the discriminant, not the one that subtracts it.
#   Round the value / return only integer value.
# Difficulty: Medium
# Date: 8/7/2021

import math

def findroots (a,b,c):

    #   If a is 0, then equation is not quadratic, but linear
    if a == 0:
        print("Invalid")
        return - 1

    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        print("Roots are real and different ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))
    elif d == 0:
        print("Roots are real and same")
        print(-b / (2 * a))
    else:  # d<0
        print("Roots are complex")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


# Driver Program
a = 1
b = -7
c = 12

# Function call
findroots(a, b, c)
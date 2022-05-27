# Return the Factorial
# Create a function that takes an integer and returns the factorial of that integer.
# That is, the integer multiplied by all positive lower integers.
# Example:
#   factorial(3) ➞ 6
#   factorial(5) ➞ 120
#   factorial(13) ➞ 6227020800
# Difficulty: Easy
# Date: 8/7/2021

import math

num = int(input("Enter number : "))

# Using a for loop

def for_factorial(num):
    factorial = 1
    if num >= 1:
        for i in range (1,num+1):
            factorial = factorial * i
    return factorial


print("For Loop Factorial: " + str(for_factorial(num)))


# Using Recursion

def recur_factorial(num):
    if num == 1:
        return num
    elif num < 1:
        return ("NA")
    else:
        return num*recur_factorial(num-1)


print("Recursion Factorial: "+str((recur_factorial(num))))

# Using math.facorial()

print("math.factorial() is : ")
print(math.factorial(int(num)))



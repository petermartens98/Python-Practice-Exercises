# Harmonic Series
# Create a function that, given a precision parameter n,
# returns the value of the partial sum of the harmonic series up to n terms.
# Example:
#   harmonic(3) ➞ 1.833
#   harmonic(1) ➞ 1.0
#   harmonic(5) ➞ 2.283
# Notes:
#   Round the result to the third decimal place.
# Difficulty: Medium
# Date: 8/7/2021

import math

def harmonic(num):
    counter = 1
    harmnum = 0
    while counter <= num:
        harmnum += (1/counter)
        counter += 1

    roundedharmnum = round(harmnum, 3)

    print(str(roundedharmnum))

harmonic(3)
harmonic(1)
harmonic(5)
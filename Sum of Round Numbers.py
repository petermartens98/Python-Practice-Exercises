# Sum of Round Numbers
# Given a number, find the "round" of each digit of the number. An integer is called "round"
# if all its digits except the leftmost (most significant) are equal to zero.
# Round numbers: 4000, 1, 9, 800, 90
# Not round numbers: 110, 707, 222, 1001
# Create a function that takes a number and returns the "round" of each digit (except if the digit is zero)
# as a string. Check out the following examples for more clarification.
# Example:
#   sum_round(101) ➞ "1 100"
#   sum_round(1234) ➞ "4 30 200 1000"
#   sum_round(54210) ➞ "10 200 4000 50000"
# Difficulty: Hard
# Date: 8/7/2021
import math

def sum_round(num):

    def reverse(num):
        rev = 0
        while (num > 0):
            digit = num % 10
            rev = (rev * 10) + digit
            num = num // 10
        return rev

    num = reverse(num)
    num = str(num)
    zero = ""
    for i in num:
        print(i+zero,end=" ")
        zero += "0"


sum_round(1234)
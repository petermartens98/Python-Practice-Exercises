# Square Every Digit
# Create a function that squares every digit of a number.
# Examples:
#   square_digits(9119) ➞ 811181
#   square_digits(2483) ➞ 416649
#   square_digits(3212) ➞ 9414
# Difficulty: Easy
# Date: 8/5/2021

digit = str(input("Enter a digit: "))

def square_digits(digit):
    for i in digit:
        sd = int(i)*int(i)
        print(sd, end="")

square_digits(digit)






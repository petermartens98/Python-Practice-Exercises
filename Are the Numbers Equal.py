# Are the Numbers Equal
# Create a function that returns True when num1 is equal to num2; otherwise return False.
# Difficulty: Very Easy
# Date: 8/5/2021

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

def equality(number1,number2):
    if number1 == number2:
        return True
    else:
        return False

print("Are these equal?: "+str(equality(number1,number2)))


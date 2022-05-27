# Basic Calculator
# Create a function that takes two numbers and
# a mathematical operator + - / * and will perform a calculation with the given numbers.
# Example:
#   calculator(2, "+", 2) ➞ 4
#   calculator(2, "*", 2) ➞ 4
#   calculator(4, "/", 2) ➞ 2

number1 = int(input("Enter your first number: "))

operator = str(input("Enter your mathematical operator: "))

number2 = int(input("Enter your second number: "))

def calculator (number1, operator, number2):

    if operator == "+":
        output = number1+number2
        return output
    elif operator == "-":
        output = number1-number2
        return output
    elif operator == "*":
        output = number1*number2
        return output
    elif operator == "/":
        if number2 == 0:
            print("Cant divide by zero!")
        else:
            output =number1/number2
            return output

print("Output: "+str(calculator(number1,operator,number2)))




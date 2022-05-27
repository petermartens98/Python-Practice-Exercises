# Length of Number
# Create a function that takes a number num and returns its length.
# Examples:
#   number_length(10) ➞ 2
#   number_length(5000) ➞ 4
#   number_length(0) ➞ 1
# Note:
#   The use of the len() function is prohibited.
# Difficulty: Medium
# Date: 8/7/2021

num = str(input("Enter number : "))

def number_length(num):

    numlist = []
    i = 0
    for i in num:
        numlist.append(i)

    numlength = 0
    for i in numlist:
        numlength += 1
    return numlength

print("number length: "+str(number_length(num)))






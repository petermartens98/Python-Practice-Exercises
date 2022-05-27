# Add the Index
# Given a list of numbers, create a function which returns the list but with each element's index in the list
# added to itself. This means you add 0 to the number at index 0, add 1 to the number at index 1, etc...
# Example:
#   add_indexes([0, 0, 0, 0, 0]) ➞ [0, 1, 2, 3, 4]
#   add_indexes([1, 2, 3, 4, 5]) ➞ [1, 3, 5, 7, 9]
#   add_indexes([5, 4, 3, 2, 1]) ➞ [5, 5, 5, 5, 5]
# Difficulty: Easy
# Date: 8/7/2021

print("Enter a list of 5 numbers")
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))

number_list = [num1, num2, num3, num4, num5]

def add_indexes(number_list):
    added_list=[]
    i = 0
    while i < len(number_list):
        added_list.insert(i, number_list[i]+i)
        i += 1

    return added_list

print()
print("Original List: "+str(number_list))
print()
print("Added List: "+str(add_indexes(number_list)))

# Letter Occurance Per string
# Create a function that takes in a sentence and a character to find.
# Return a dictionary of the string, with the number of the specified character as the value.
# Difficulty: Easy
# Date: 8/5/2021

search_string = input("Enter a string: ")
search_character = input("Enter a character: ")

def find_occurances(search_string, search_character):
    occurances = 0
    for i in search_string:
        if i == search_character:
            occurances += 1

    return occurances

string_occurances = str(find_occurances(search_string, search_character))

print(search_character+" occurs in "+search_string+" "+string_occurances+" times")

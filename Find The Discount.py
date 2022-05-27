# Find the Discount
# Create a function that takes two arguments:
# the original price and the discount percentage as integers and returns the final price after the discount.
# Examples:
#   dis(1500, 50) ➞ 750
#   dis(89, 20) ➞ 71.2
#   dis(100, 75) ➞ 25
# Difficulty: Easy
# Date: 8/7/2021

original_price = int(input("Enter the original price: "))
percent_discount = int(input("Enter the percent discount: "))
percent_discount = percent_discount/100

def discouned_price (original_price, percent_discount):
    price = original_price * (1 - percent_discount)
    return price

print("The discounted price is: "+str(discouned_price(original_price,percent_discount)))


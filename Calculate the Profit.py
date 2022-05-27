# Calculate the Profit
# You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars),
# and the starting inventory. Return the total profit made, rounded to the nearest dollar.
# Example:
#   profit({
#       "cost_price": 32.67,
#       "sell_price": 45.00,
#       "inventory": 1200
#   }) ➞ 14796
#
#   profit({
#       "cost_price": 225.89,
#       "sell_price": 550.00,
#       "inventory": 100
#   }) ➞ 32411
#
# Notes:
#   Assume all inventory has been sold.
#   Profit = Total Sales - Total Cost
# Difficulty: Medium
# Date: 8/7/2021

cost_price = float(input("Enter cost price: "))
sell_price = float(input("Enter sell price: "))
inventory = int(input("Enter inventory: "))

def profit(cost_price,sell_price,inventory):
    profits = sell_price - cost_price
    profits = profits*inventory
    format(profits,'.2f')
    return profits

print()
print("Profits: "+str(profit(cost_price,sell_price,inventory)))



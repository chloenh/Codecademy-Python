#Define a function compute_bill that takes one argument food as input.

#In the function, create a variable total with an initial value of zero.

#For each item in the food list, add the price of that item to total.

#Finally, return the total.

shopping_list = ["banana", "orange", "apple"]

stock = {
  "banana": 6,
  "apple": 0,
  "orange": 32,
  "pear": 15
}
    
prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
    return total

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

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        check_stock = stock[item]
        if check_stock > 0:
            cost = prices[item]
            total += cost
            stock[item] -= 1
    return total


print stock
print compute_bill(["apple", "banana", "pear"])
print stock
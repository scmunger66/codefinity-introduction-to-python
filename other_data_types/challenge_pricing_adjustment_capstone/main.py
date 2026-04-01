grocery_inventory = {
    "Milk": ("Dairy", 3.50, 8),
    "Eggs": ("Dairy", 5.50, 30),
    "Bread": ("Bakery", 2.99, 15),
    "Apples": ("Produce", 1.50, 50)}

print(grocery_inventory)
# Check and update price
egg_price = grocery_inventory["Eggs"][1]
if egg_price >= 5:
    print("Eggs are too expensive, reducing the price by $1")
    category, old_price, stock = grocery_inventory["Eggs"]
    grocery_inventory["Eggs"] = (category, old_price -1, stock)

print(grocery_inventory)
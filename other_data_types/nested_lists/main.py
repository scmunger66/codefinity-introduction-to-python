vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print(vegetables)
updated_vegetable_inventory = vegetables
print(updated_vegetable_inventory)
if "carrots" not in updated_vegetable_inventory:
    vegetables.append("carrots")
    print("Carrots are already in the list.")
if "cucumbers" not in updated_vegetable_inventory:
    vegetables.append("cucumber")
    print("Cucumbers are already in the list.") 
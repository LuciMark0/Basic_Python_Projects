import random

items = ["rope", "coin", "stick", "rock", "string", "meat"]
inventory = {}
chest = {}

def chestOpening(amountItem=random.randint(1, 10)):
    for _ in range(amountItem):
        item = random.choice(items)
        chest[item] = chest.get(item, 0) + 1

    for item, quantity in chest.items():
        inventory[item] = inventory.get(item, 0) + quantity

    chest.clear()
    print_inventory()

def print_item():
    item = input("Which item are you looking for: ").lower()
    quantity = inventory.get(item, 0)

    if quantity == 0:
        print(f"The adventurer doesn't have a {item}")
    else:
        print(f"{item.capitalize()}: {quantity}")

def print_inventory():
    print("-- Items in inventory --")
    for item, quantity in inventory.items():
        print(f"{item.capitalize()}: {quantity}")

try:
    while True:
        input("Press Enter to open the chest (Ctrl+D or Ctrl+Z to exit): ")
        chestOpening()
        print_item()

except EOFError:
    print("\nExiting the game...")
import json, os

DATA_FILE = "data/inventory.json"

def load_inventory():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_inventory(inventory):
    with open(DATA_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def add_item():
    inventory = load_inventory()
    name = input("Enter item name: ").strip()
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    inventory[name] = {"quantity": qty, "price": price}
    save_inventory(inventory)
    print(f"{name} added successfully!")

def view_inventory():
    inventory = load_inventory()
    if not inventory:
        print("Inventory is empty.")
        return
    print("\n--- Current Inventory ---")
    for name, details in inventory.items():
        print(f"{name:15} | Qty: {details['quantity']:3} | Price: ₹{details['price']:.2f}")

def update_item():
    inventory = load_inventory()
    name = input("Enter item name to update: ").strip()
    if name not in inventory:
        print("Item not found!")
        return
    qty = int(input("Enter new quantity: "))
    inventory[name]["quantity"] = qty
    save_inventory(inventory)
    print(f"{name} updated successfully!")

def delete_item():
    inventory = load_inventory()
    name = input("Enter item name to delete: ").strip()
    if name in inventory:
        del inventory[name]
        save_inventory(inventory)
        print(f"{name} deleted successfully!")
    else:
        print("Item not found.")

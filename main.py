from invoicing import generate_invoice
from inventory import view_inventory

def main():
    print("=== Invoice Generator ===")
    view_inventory()

    customer = input("Enter customer name: ")
    purchased_items = []

    while True:
        item_id = int(input("Enter item ID to buy (0 to finish): "))
        if item_id == 0:
            break
        qty = int(input("Enter quantity: "))
        purchased_items.append({"item_id": item_id, "quantity": qty})

    generate_invoice(customer, purchased_items)
    print("\nUpdated Inventory:")
    view_inventory()

if __name__ == "__main__":
    main()

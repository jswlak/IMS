from inventory_utils import add_item, view_inventory, update_item, delete_item

def main():
    while True:
        print("\n=== Inventory Management ===")
        print("1. Add Item")
        print("2. View Inventory")
        print("3. Update Quantity")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            add_item()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()

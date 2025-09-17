SHOP_FILE = "/home/user/Desktop/Python/file handling/Shopping Expense Tracker/shop.txt"

def expensive_tracker():
    shop_item = []
    try:
        with open(SHOP_FILE, "r") as f:
            for line in f:
                item_name, quantity, price = line.strip().split("|")
                shop_item.append({
                    "item_name": item_name,
                    "quantity": int(quantity),
                    "price": float(price)
                })
    except FileNotFoundError:
        pass  
    return shop_item


def save_item(shop_item):
    with open(SHOP_FILE, "w") as f:
        for i in shop_item:
            f.write(f"{i['item_name']}|{i['quantity']}|{i['price']}\n")


def add_item(shop_item):
    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price per unit: "))
    
    shop_item.append({
        "item_name": item_name,
        "quantity": quantity,
        "price": price
    })
    
    save_item(shop_item)
    print(" Item saved successfully!")


def view_all(shop_item):
    if not shop_item:
        print(" No items stored yet.")
        return
    print("\n--- Shopping Items ---")
    for c in shop_item:
        print(f"Item: {c['item_name']}, Quantity: {c['quantity']}, Price per unit: ₹{c['price']}")


def calculate_total(shop_item):
    if not shop_item:
        print(" No items to calculate.")
        return
    total = sum(c['quantity'] * c['price'] for c in shop_item)
    print(f"\n Total Expenses: ₹{total:.2f}")


def main():
    items = expensive_tracker()
    while True:
        print("\n=== Shopping Expense Tracker ===")
        print("1. Add New Item")
        print("2. View All Items")
        print("3. Calculate Total Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_item(items)
        elif choice == "2":
            view_all(items)
        elif choice == "3":
            calculate_total(items)
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice, please try again.")


if __name__ == "__main__":
    main()

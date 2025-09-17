def load_contacts():
    contacts = []
    try:
        with open("/home/user/Desktop/Python/file handling/simple Contact Manager/contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split("|")
                contacts.append({"name": name, "phone": phone, "email": email})
    except FileNotFoundError:
        pass  
    return contacts


def save_contacts(contacts):
    with open("/home/user/Desktop/Python/file handling/simple Contact Manager/contacts.txt", "w") as f:
        for c in contacts:
            f.write(f"{c['name']}|{c['phone']}|{c['email']}\n")


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(" Contact added successfully!")


def view_contacts(contacts):
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- All Contacts ---")
        i = 1
        for c in contacts:
            print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")
            i += 1
        print("--------------------\n")


def search_contact(contacts):
    name = input("Enter name to search: ")
    found = [c for c in contacts if c['name'].lower() == name.lower()]
    if found:
        for c in found:
            print(f"Found: {c['name']} | {c['phone']} | {c['email']}")
    else:
        print(" Contact not found.")


def remove_contact(contacts):
    name = input("Enter name to remove: ")
    updated_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(updated_contacts) < len(contacts):
        save_contacts(updated_contacts)
        print(" Contact removed successfully!")
    else:
        print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Remove Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            remove_contact(contacts)
            contacts = load_contacts() 
        elif choice == "5":
            print("See You Soon!")
            break
        else:
            print(" Invalid choice, please try again.")


if __name__ == "__main__":
    main()

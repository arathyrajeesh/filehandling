PASSWORD_FILE = "/home/user/Desktop/Python/file handling/Simple Password Manager/passwords.txt"

def load_credentials():
    credentials = []
    try:
        with open(PASSWORD_FILE, "r") as f:
            for line in f:
                website, username, password = line.strip().split("|")
                credentials.append({"website": website, "username": username, "password": password})
    except FileNotFoundError:
        pass  
    return credentials

def save_credentials(credentials):
    with open(PASSWORD_FILE, "w") as f:
        for i in credentials:
            f.write(f"{i['website']}|{i['username']}|{i['password']}\n")

def add_credentials(credentials):
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    credentials.append({"website": website, "username": username, "password": password})
    save_credentials(credentials)
    print(" Credentials saved successfully!")

def view_credentials(credentials):
    website = input("Enter website to search: ").lower()
    found = [c for c in credentials if c["website"].lower() == website]
    if found:
        for c in found:
            print(f"Website: {c['website']}, Username: {c['username']}, Password: {c['password']}")
    else:
        print(" No credentials found for that website.")

def view_all(credentials):
    if not credentials:
        print("No credentials stored yet.")
        return
    for c in credentials:
        print(f"Website: {c['website']}, Username: {c['username']}, Password: {c['password']}")

def main():
    credentials = load_credentials()
    while True:
        print("\n--- Password Manager ---")
        print("1. Add New Credentials")
        print("2. View Credentials for a Website")
        print("3. View All Credentials")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_credentials(credentials)
        elif choice == "2":
            view_credentials(credentials)
        elif choice == "3":
            view_all(credentials)
        elif choice == "4":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

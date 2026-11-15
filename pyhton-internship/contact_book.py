contacts = {}
while True:
    print("\n1. Add  2. View  3. Search  4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        if name and phone:
            contacts[name.lower()] = (name, phone)
            print("Contact saved.")
        else:
            print("Name and phone are required.")
    elif choice == "2":
        if not contacts:
            print("No contacts saved.")
        else:
            for name, phone in contacts.values():
                print(f"{name}: {phone}")
    elif choice == "3":
        name = input("Search name: ").strip().lower()
        if name in contacts:
            saved_name, phone = contacts[name]
            print(f"{saved_name}: {phone}")
        else:
            print("Contact not found.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")

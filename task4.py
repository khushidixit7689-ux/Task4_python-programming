# Contact Management System

contacts = []  # List to store all contacts


def add_contact():
    """Add a new contact"""
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"\nContact '{name}' added successfully!\n")


def view_contacts():
    """View all contacts (Name + Phone)"""
    if not contacts:
        print("\n No contacts found!\n")
        return

    print("\n Contact List:")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")
    print()


def search_contact():
    """Search by name or phone"""
    query = input(" Enter name or phone to search: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name    : {contact['name']}")
            print(f"Phone   : {contact['phone']}")
            print(f"Email   : {contact['email']}")
            print(f"Address : {contact['address']}\n")
            found = True
    if not found:
        print("\n No contact found!\n")


def update_contact():
    """Update existing contact"""
    phone = input("Enter phone number of contact to update: ")
    for contact in contacts:
        if contact['phone'] == phone:
            print("\nLeave blank to keep existing value.\n")
            name = input(f"Enter New Name ({contact['name']}): ") or contact['name']
            email = input(f"Enter New Email ({contact['email']}): ") or contact['email']
            address = input(f"Enter New Address ({contact['address']}): ") or contact['address']

            contact['name'] = name
            contact['email'] = email
            contact['address'] = address

            print("\nContact updated successfully!\n")
            return
    print("\n Contact not found!\n")


def delete_contact():
    """Delete a contact by phone number"""
    phone = input("Enter phone number of contact to delete: ")
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print(f"\n Contact '{contact['name']}' deleted successfully!\n")
            return
    print("\n Contact not found!\n")


def menu():
    """Main menu loop"""
    while True:
        print("======  Contact Management System ======")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n Exiting... Have a nice day!\n")
            break
        else:
            print("\n Invalid choice, please try again!\n")


# Run program
menu()

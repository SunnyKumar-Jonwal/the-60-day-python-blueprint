CONTACTS_FILE = "day-20/project/contacts.txt"


def load_contacts(path):
    contacts = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, phone, email = line.split(",")
            contacts.append({"name": name, "phone": phone, "email": email})
    return contacts


def save_contacts(path, contacts):
    with open(path, "w") as file:
        for contact in contacts:
            file.write(f"{contact['name']},{contact['phone']},{contact['email']}\n")


def add_contact(contacts):
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email})
    print(f"Added {name}.")


def list_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
        return
    for contact in contacts:
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def search_contacts(contacts):
    query = input("Search for: ").strip().lower()
    matches = [c for c in contacts if query in c["name"].lower()]
    if not matches:
        print("No matches.")
        return
    for contact in matches:
        print(f"{contact['name']} | {contact['phone']} | {contact['email']}")


def delete_contact(contacts):
    name = input("Name to delete: ").strip()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print(f"Deleted {name}.")
            return
    print(f"No contact named {name} found.")


def print_menu():
    print("\n1. Add contact")
    print("2. List contacts")
    print("3. Search contacts")
    print("4. Delete contact")
    print("5. Quit")


def main():
    contacts = load_contacts(CONTACTS_FILE)
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(CONTACTS_FILE, contacts)
            print("Contacts saved. Goodbye!")
            break
        else:
            print("Invalid option, try again.")


main()

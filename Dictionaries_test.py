#Exercise: Create a Dictionary for a Contact List

#Create a Python program that simulates a simple contact list using a dictionary. Each contact will have a name as the key and a phone number as the value. Your program should allow users to perform the following operations:

#Add a new contact.
#Remove an existing contact by name.
#Lookup a contact by name to retrieve their phone number.
#List all contacts and their phone numbers.
#Exit the program.

contacts = {}

while True:
    print("\nContact List Menu:")
    print("1. Add a new contact")
    print("2. Remove a contact")
    print("3. Lookup a contact")
    print("4. List all contacts")
    print("5. Exit")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        # Add a new contact
        name = input("Enter the name: ")
        phone_number = input("Enter the phone number: ")
        contacts[name] = phone_number
        print(f"Contact '{name}' added successfully.")

    elif choice == '2':
        # Remove a contact
        name = input("Enter the name of the contact to remove: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' removed successfully.")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '3':
        # Lookup a contact
        name = input("Enter the name to lookup: ")
        if name in contacts:
            print(f"Phone number for '{name}': {contacts[name]}")
        else:
            print(f"Contact '{name}' not found.")

    elif choice == '4':
        # List all contacts
        print("\nContact List:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")

    elif choice == '5':
        # Exit the program
        print("Exiting the contact list program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option (1/2/3/4/5).")
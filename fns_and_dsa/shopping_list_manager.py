def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            add_item = input("Enter the item to add: ")
            shopping_list.append(add_item)
            print("Item added successfully!")

        elif choice == '2':
            # Prompt for and remove an item
            delete_item = input("Enter the item to delete: ")
            for i in shopping_list:
                if i == delete_item:
                    shopping_list.remove(delete_item)
                    print("Item deleted successfully!")
                else:
                    print("No such item found!")

        elif choice == '3':
            # Display the shopping list
            print(shopping_list)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

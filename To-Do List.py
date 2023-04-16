to_do_list = []

def add_to_do_item():
    item = input("Enter a to-do item: ")
    to_do_list.append(item)

def display_to_do_list():
    print("To-Do List:")
    for i, item in enumerate(to_do_list):
        print(f"{i+1}. {item}")

def remove_to_do_item():
    display_to_do_list()
    index = int(input("Enter the index of the item to remove: ")) - 1
    del to_do_list[index]

def clear_to_do_list():
    confirm = input("Are you sure you want to clear the list? (y/n): ")
    if confirm.lower() == "y":
        to_do_list.clear()

def show_menu():
    print("To-Do List Menu")
    print("1. Add to-do task")
    print("2. Display to-do list")
    print("3. Remove to-do item")
    print("4. Clear to-do list")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    return choice

while True:
    choice = show_menu()
    if choice == 1:
        add_to_do_item()
    elif choice == 2:
        display_to_do_list()
    elif choice == 3:
        remove_to_do_item()
    elif choice == 4:
        clear_to_do_list()
    elif choice == 5:
        break
    else:
        print("Invalid choice. Please try again.")

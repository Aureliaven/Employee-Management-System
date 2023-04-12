def add_new_employee():
    print("Adding New Employee!")

def update_employee():
    print("Updating Employee!")


def remove_employee():
    print("Removing Employee!")

def list_employees():
    print("Listing Employees!")


while True:
    print("Please select a option:")
    print("1. Add a new employee")
    print("2. Update an existing employee")
    print("3. Remove an employee")
    print("4. Show all employees")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            raise ValueError
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        add_new_employee()

    elif choice == 2:
        update_employee()

    elif choice == 3:
        remove_employee()

    elif choice == 4:
        list_employees()

    elif choice == 5:
        print("Goodbye!")
        break
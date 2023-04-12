import io
import employee

class InvalidChoice(Exception):
    pass

employees = []
try:
    with open("./employees.csv") as f:
        company_name = f.readline().strip()
        id_counter = int(f.readline().strip())
        for line in f.readlines():
            values = line.strip().split(",")
            employees.append(employee.Employee(int(values[0]),values[1],values[2],values[3],int(values[4]),values[5]))
except FileNotFoundError:
    while True:
        company_name = input("What is the name of your company? ")
        if not company_name:
            print("Company name cannot be empty.\n")
            continue
        break
    id_counter = 1
    employees = []
except io.UnsupportedOperation:
    print("Something went wrong :/\n")

def add_new_employee():
    global employees
    global id_counter
    employee = employee.Employee()
    employee.set_new_id()
    employee.set_first_name()
    employee.set_last_name()
    employee.set_join_date()
    employee.set_salary()
    employee.set_department()
    employees.append(employee)
    print(f"\n{employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}) was added.\n")

def update_employee():
    global employees
    while True:
        print("\nWhich employee would you like to update?\n")
        for e in employees:
            print(f"{e.get_id()}. {e}")
        print("#. Exit\n")
        try:
            e_id = input(": ")
            if e_id == "#":
                break
            if not e_id.isnumeric():
                raise ValueError
            employee = None
            for e in employees:
                if int(e_id) == e.get_id():
                    employee = e
            if not employee:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid employee id.\n")
            continue
        except ValueError:
            print("Employee id must be a number.\n")
        
        while True:
            print("\nPlease select a option:")
            print("1. Change first name")
            print("2. Change last name")
            print("3. Change salary")
            print("4. Change department")
            print("5. Exit\n")
            try:
                choice = input("Enter your choice: ")
                if not choice.isnumeric():
                    raise ValueError
                choice = int(choice)
                if choice < 1 or choice > 5:
                    raise InvalidChoice
            except InvalidChoice:
                print("Invalid choice. Please enter a number between 1 and 5.\n")
                continue

            if choice == 1:
                print(f"\nSetting new first name for {employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}).")
                employee.set_first_name()

            elif choice == 2:
                print(f"\nSetting new last name for {employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}).")
                employee.set_last_name()

            elif choice == 3:
                print(f"\nSetting new salary for {employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}).")
                employee.set_salary()

            elif choice == 4:
                print(f"\nSetting new department for {employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}).")
                employee.set_department()

            else:
                break

def remove_employee():
    global employees
    print(employees)
    while True:
        print("\nWhich employee would you like to remove?\n")
        for e in employees:
            print(f"{e.get_id()}. {e}")
        print("#. Exit\n")
        try:
            e_id = input(": ")
            if e_id == "#":
                break
            if not e_id.isnumeric():
                raise ValueError
            employee = None
            for i in range(len(employees)):
                if int(e_id) == employees[i].get_id():
                    print(f"\n{employees[i].get_first_name()} {employees[i].get_last_name()} was successfully removed.")
                    employee = employees.pop(i)
                    break
            if not employee:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid employee id.\n")
            continue
        except ValueError:
            print("Employee id must be a number.\n")

def list_employees():
    global company_name
    print(f"\n{company_name} employees: \n")
    for e in employees:
        print(e)
    print()

while True:
    print(f"\nWelcome, {company_name}.\n")
    print("Please select a option:")
    print("1. Add a new employee")
    print("2. Update an existing employee")
    print("3. Remove an employee")
    print("4. Show all employees")
    print("5. Exit\n")

    try:
        choice = input("Enter your choice: ")
        if not choice.isnumeric():
            raise ValueError
        choice = int(choice)
        if choice < 1 or choice > 5:
            raise InvalidChoice
    except InvalidChoice:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
        continue
    except ValueError:
        print("Choice must be a number.\n")
        continue

    if choice == 1:
        add_new_employee()

    elif choice == 2:
        update_employee()

    elif choice == 3:
        remove_employee()

    elif choice == 4:
        list_employees()

    else:
        with open("./employees.csv", "w") as f:
            f.write(company_name + "\n")
            f.write(str(id_counter) + "\n")
            for e in employees:
                f.write(f"{e.get_id()},{e.get_first_name()},{e.get_last_name()},{e.get_join_date()},{e.get_salary()},{e.get_department()}\n")
        print("\nEmployee info saved to file.\n")
        break
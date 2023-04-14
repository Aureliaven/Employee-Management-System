import io
import employee as emp
import department as dep

class InvalidChoice(Exception):
    pass

employees = []
departments = []
try:
    with open("./employees.csv") as f:
        company_name = f.readline().strip()
        eid_counter = int(f.readline().strip())
        for line in f.readlines():
            values = line.strip().split(",")
            employees.append(emp.Employee(int(values[0]),values[1],values[2],values[3],int(values[4]),values[5]))
except FileNotFoundError:
    while True:
        company_name = input("What is the name of your company? ")
        if not company_name:
            print("Company name cannot be empty.\n")
            continue
        break
    eid_counter = 1
    employees = []
except io.UnsupportedOperation:
    print("Something went wrong :/\n")

try:
    with open("./departments.csv") as f:
        did_counter = int(f.readline().strip())
        for line in f.readlines():
            values = line.strip().split(",")
            departments.append(dep.Department(int(values[0]),values[1],int(values[2]),values[3]))
except FileNotFoundError:
    did_counter = 1
    departments = []
except io.UnsupportedOperation:
    print("Something went wrong :/\n")

def set_emp_dep(employee: emp.Employee):
    global departments
    while True:
        print(f"Choose a department for {employee.get_first_name()} {employee.get_last_name()}: \n")
        for d in departments:
            print(f"{d.get_id()} - {d}")
        print("# - Exit\n")
        try:
            d_id = input(": ")
            if d_id == "#":
                break
            if not d_id.isnumeric():
                raise ValueError
            department = None
            for d in departments:
                if int(d_id) == d.get_id():
                    department = d
            if not department:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid department id.\n")
            continue
        except ValueError:
            print("Department id must be a number.\n")
            continue
        employee.set_department(department.get_name())
        print(f"\n{employee.get_first_name()} {employee.get_last_name()} (ID {employee.get_id()}) was added to {department.get_name()}.\n")
        break

def add_employee():
    global employees
    global departments
    global eid_counter
    if not departments:
        print("\nYou must create a department first!\n")
        return
    employee = emp.Employee()
    employee.set_id(eid_counter)
    eid_counter += 1
    employee.set_first_name()
    employee.set_last_name()
    employee.set_join_date()
    employee.set_salary()
    set_emp_dep(employee)
    employees.append(employee)

def update_employee():
    global employees
    global departments
    if not employees:
        print("\nYou have no employees to update.\n")
        return
    if not departments:
        print("\nYou must create a department first!\n")
        return
    while True:
        print("\nWhich employee would you like to update?\n")
        for e in employees:
            print(f"{e.get_id()} - {e}")
        print("# - Exit\n")
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
            print("1 - Change first name")
            print("2 - Change last name")
            print("3 - Change salary")
            print("4 - Change department")
            print("# - Exit\n")
            try:
                choice = input("Enter your choice: ")
                if choice == "#":
                    break
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
                set_emp_dep(employee)

def remove_employee():
    global employees
    if not departments:
        print("\nYou must create a department first!\n")
        return
    while True:
        if not employees:
            print("\nYou currently have no employees.\n")
            return
        print("\nWhich employee would you like to remove?\n")
        for e in employees:
            print(f"{e.get_id()} - {e}")
        print("# - Exit\n")
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
    global employees
    if not employees:
        print("\nYou have no employees to view.\n")
        return
    print(f"\n{company_name} employees: \n")
    for e in employees:
        print(e)
    print()

def add_department():
    global departments
    global did_counter
    department = dep.Department()
    department.set_id(did_counter)
    did_counter += 1
    department.set_name()
    department.set_budget()
    department.set_phone()
    departments.append(department)
    print(f"\nThe {department.get_name()} department (ID {department.get_id()}) was added.\n")

def update_department():
    global departments
    if not departments:
        print("\nYou have no departments to update.\n")
        return
    while True:
        print("\nWhich department would you like to update?\n")
        for d in departments:
            print(f"{d.get_id()} - {d}")
        print("# - Exit\n")
        try:
            d_id = input(": ")
            if d_id == "#":
                break
            if not d_id.isnumeric():
                raise ValueError
            department = None
            for d in departments:
                if int(d_id) == d.get_id():
                    department = d
            if not department:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid department id.\n")
            continue
        except ValueError:
            print("Department id must be a number.\n")
        
        while True:
            print("\nPlease select a option:")
            print("1 - Change department name")
            print("2 - Change annual budget")
            print("3 - Change phone number")
            print("# - Exit\n")
            try:
                choice = input("Enter your choice: ")
                if choice == "#":
                    break
                if not choice.isnumeric():
                    raise ValueError
                choice = int(choice)
                if choice < 1 or choice > 3:
                    raise InvalidChoice
            except InvalidChoice:
                print("Invalid choice. Please enter a number between 1 and 3.\n")
                continue

            if choice == 1:
                print(f"\nSetting new name for {department.get_name()} (ID ({department.get_id()}).")
                department.set_name()

            elif choice == 2:
                print(f"\nSetting new annual budget for {department.get_name()} (ID ({department.get_id()}).")
                department.set_budget()

            elif choice == 3:
                print(f"\nSetting new phone number for {department.get_name()} (ID ({department.get_id()}).")
                department.set_phone()

def remove_department():
    global departments
    global employees
    while True:
        if not departments:
            print("\nYou currently have no departments.\n")
            return
        print("\nWhich department would you like to remove?\n")
        for d in departments:
            print(f"{d.get_id()} - {d}")
        print("# - Exit\n")
        try:
            d_id = input(": ")
            if d_id == "#":
                break
            if not d_id.isnumeric():
                raise ValueError
            department = None
            for i in range(len(departments)):
                if int(d_id) == departments[i].get_id():
                    department = departments[i]
                    e_in_d = [e for e in employees if e.get_department() == department.get_name()]
                    if e_in_d:
                        print(f"\n{department.get_name()} has {len(e_in_d)} active employees. Are you sure you want to delete this department?\n")
                        while True:
                            try:
                                response = str(input("(Y/N): "))
                                if not response:
                                    raise InvalidChoice
                                elif not response.isalpha():
                                    raise ValueError
                                response = response.lower()
                                if response != "y" and response != "n":
                                    raise InvalidChoice
                            except InvalidChoice:
                                print("Choice must be Y or N.\n")
                                continue
                            except ValueError:
                                print("Choice must be a letter.\n")
                                continue
                            if response == "y":
                                eids = [eid.get_id() for eid in e_in_d]
                                employees = [e for e in employees if e.get_id() not in eids]
                                print(f"\nEmployees of the {department.get_name()} department were removed.")
                                print(f"\n{department.get_name()} was successfully removed.")
                                departments.pop(i)
                            elif response == "n":
                                break
                            break
                    break
            if not department:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid department id.\n")
            continue
        except ValueError:
            print("Department id must be a number.\n")
            continue

def list_departments():
    global company_name
    global departments
    global employees
    if not departments:
        print("\nYou have no departments to view.\n")
        return
    print(f"\n{company_name} departments: \n")
    while True:
        print("Which department would you like to view?\n")
        for d in departments:
            print(f"{d.get_id()} - {d}")
        print("# - Exit\n")
        try:
            d_id = input(": ")
            if d_id == "#":
                break
            if not d_id.isnumeric():
                raise ValueError
            department = None
            for d in departments:
                if int(d_id) == d.get_id():
                    department = d
            if not department:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid department id.\n")
            continue
        except ValueError:
            print("Department id must be a number.\n")
            continue
        print(f"\nEmployees in {department.get_name()}:\n")
        e_in_d = [e for e in employees if e.get_department() == department.get_name()]
        for i in e_in_d:
            print(i)
        print()

while True:
    print(f"\nWelcome, {company_name}.\n")
    print("Please select a option:")
    print("1 - View/modify employees")
    print("2 - View/modify departments")
    print("# - Exit\n")

    try:
        choice = input("Enter your choice: ")
        if choice == "#":
            with open("./employees.csv", "w") as f:
                f.write(company_name + "\n")
                f.write(str(eid_counter) + "\n")
                for e in employees:
                    f.write(f"{e.get_id()},{e.get_first_name()},{e.get_last_name()},{e.get_join_date()},{e.get_salary()},{e.get_department()}\n")
            print("\nEmployee info saved to file.")
            with open("./departments.csv", "w") as f:
                f.write(str(did_counter) + "\n")
                for d in departments:
                    f.write(f"{d.get_id()},{d.get_name()},{d.get_budget()},{d.get_phone()}\n")    
            print("Department info saved to file.\n")
            break
        if not choice.isnumeric():
            raise ValueError
        choice = int(choice)
        if choice < 1 or choice > 2:
            raise InvalidChoice
    except InvalidChoice:
        print("Invalid choice. Please enter 1 or 2.\n")
        continue
    except ValueError:
        print("Choice must be a number (1 or 2).\n")
        continue

    if choice == 1:
        while True:
            print("\nPlease select an option:")
            print("1 - Add an employee")
            print("2 - Update employee info")
            print("3 - Remove an employee")
            print("4 - View all employees")
            print("# - Exit")
            try:
                choice = input("Enter your choice: ")
                if choice == "#":
                    break
                if not choice.isnumeric():
                    raise ValueError
                choice = int(choice)
                if choice < 1 or choice > 4:
                    raise InvalidChoice
            except InvalidChoice:
                print("Invalid choice. Please enter a number between 1 and 4.\n")
                continue
            except ValueError:
                print("Choice must be a number.\n")
                continue

            if choice == 1:
                add_employee()
            
            elif choice == 2:
                update_employee()

            elif choice == 3:
                remove_employee()

            elif choice == 4:
                list_employees()


    elif choice == 2:
        while True:
            print("\nPlease select an option:")
            print("1 - Add a department")
            print("2 - Update department info")
            print("3 - Remove a department")
            print("4 - View all departments")
            print("# - Exit")
            try:
                choice = input("Enter your choice: ")
                if choice == "#":
                    break
                if not choice.isnumeric():
                    raise ValueError
                choice = int(choice)
                if choice < 1 or choice > 4:
                    raise InvalidChoice
            except InvalidChoice:
                print("Invalid choice. Please enter a number between 1 and 4.\n")
                continue
            except ValueError:
                print("Choice must be a number.\n")
                continue
            
            if choice == 1:
                add_department()
            
            elif choice == 2:
                update_department()

            elif choice == 3:
                remove_department()

            elif choice == 4:
                list_departments()
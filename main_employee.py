import datetime
import io

class InvalidChoice(Exception):
    pass

class Employee:
    def __init__(self, id=0, first_name="First", last_name="Last", join_date="Date", salary=0, department="Department"):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.join_date = join_date
        self.salary = salary
        self.department = department

    def __str__(self):
        return f"{self.first_name} {self.last_name} from {self.department}, joined {self.join_date} and makes ${self.salary}"

    def set_new_id(self):
        global id_counter
        self.id = id_counter
        id_counter += 1

    def set_id(self, id):
        self.id = id
    
    def set_first_name(self):
        while True:
            first_name = input("Employee first name: ")
            if not first_name:
                print("Name cannot be empty!")
                continue
            if not first_name.isalpha():
                print("Name cannot contain numbers or symbols!")
                continue
            else:
                self.first_name = first_name
                break

    def set_last_name(self):
        while True:
            last_name = input("Employee last name: ")
            if not last_name:
                print("Name cannot be empty!")
                continue
            if not last_name.isalpha():
                print("Name cannot contain numbers or symbols!")
                continue
            else:
                self.last_name = last_name
                break

    def set_join_date(self):
        date = datetime.datetime.now()
        self.join_date = date.strftime("%x")

    def set_salary(self):
        while True:
            salary = input("Employee salary: ")
            if not salary:
                print("Salary cannot be empty or zero!")
                continue
            if not salary.isnumeric():
                print("Salary cannot contain letters or symbols!")
                continue
            else:
                self.salary = salary
                break

    def set_department(self):
        while True:
            department = input("Employee department: ")
            if not department:
                print("Department cannot be empty!")
                continue
            if not department.isalpha():
                print("Department cannot contain numbers or symbols!")
                continue
            else:
                self.department = department
                break

    def get_id(self):
        return self.id
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_join_date(self):
        return self.join_date
    
    def get_salary(self):
        return self.salary
    
    def get_department(self):
        return self.department

employees = []
try:
    with open("./employees.csv") as f:
        company_name = f.readline().strip()
        id_counter = int(f.readline().strip())
        employees.append()
        for line in f.readlines():
            values = line.strip().split(",")
            employees.append(Employee(int(values[0]),values[1],values[2],values[3],int(values[4]),values[5]))
except FileNotFoundError:
    while True:
        company_name = input("What is the name of your company? ")
        if not company_name:
            print("Company name cannot be empty.")
            continue
        else:
            print(f"\nWelcome, {company_name}.\n")
            break
    id_counter = 1
    employees = []
except io.UnsupportedOperation:
    print("Something went wrong :/")

def add_new_employee():
    global employees
    global id_counter
    employee = Employee()
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
            employee = None
            for e in employees:
                if int(e_id) == e.get_id():
                    employee = e
            if not employee:
                raise InvalidChoice
        except InvalidChoice:
            print("Invalid employee id!\n")
            continue
        
        while True:
            print("\nPlease select a option:")
            print("1. Change first name")
            print("2. Change last name")
            print("3. Change salary")
            print("4. Change department")
            print("5. Exit\n")
            try:
                choice = int(input("Enter your choice: "))
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
            for i in range(len(employees)):
                if int(e_id) == employees[i].get_id():
                    print(f"\n{employees[i].get_first_name()} {employees[i].get_last_name()} was successfully removed.")
                    employees.pop(i)
                    break
        except ValueError:
            print("Invalid employee id!\n")
            continue

def list_employees():
    global company_name
    print(f"\n{company_name} employees: \n")
    for e in employees:
        print(e)
    print()

while True:
    print("\nPlease select a option:")
    print("1. Add a new employee")
    print("2. Update an existing employee")
    print("3. Remove an employee")
    print("4. Show all employees")
    print("5. Exit\n")

    try:
        choice = int(input("Enter your choice: "))
        if choice < 1 or choice > 5:
            raise InvalidChoice
    except InvalidChoice:
        print("Invalid choice. Please enter a number between 1 and 5.\n")
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
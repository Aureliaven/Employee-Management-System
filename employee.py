import datetime

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
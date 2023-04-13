import datetime
import re

class Employee:
    def __init__(self, id=0, first_name="First", last_name="Last", join_date="Date", salary=0, department="Department"):
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__join_date = join_date
        self.__salary = salary
        self.__department = department

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} from {self.__department}, joined {self.__join_date} and makes ${self.__salary}"

    def set_id(self, id):
        self.__id = id
    
    def set_first_name(self):
        while True:
            first_name = input("Employee first name: ")
            if not first_name:
                print("Name cannot be empty!")
                continue
            if not re.search("^[A-Za-z-']+$", first_name):
                print("Name cannot contain spaces, numbers, or symbols! (except - and ')")
                continue
            else:
                self.__first_name = first_name
                break

    def set_last_name(self):
        while True:
            last_name = input("Employee last name: ")
            if not last_name:
                print("Name cannot be empty!")
                continue
            if not re.search("^[A-Za-z-']+$", last_name):
                print("Name cannot contain spaces, numbers, or symbols! (except - and ')")
                continue
            else:
                self.__last_name = last_name
                break

    def set_join_date(self):
        date = datetime.datetime.now()
        self.__join_date = date.strftime("%x")

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
                self.__salary = salary
                break

    def set_department(self, department):
        self.__department = department

    def get_id(self):
        return self.__id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_join_date(self):
        return self.__join_date
    
    def get_salary(self):
        return self.__salary
    
    def get_department(self):
        return self.__department
class Department:
    def __init__(self, name, budget, phone):
        self.__name = name
        self.__budget = budget
        self.__phone = phone
    
    def __str__(self):
        return f"{self.__name} has an annual budget of ${self.__budget}. Contact number: {self.__phone}."
    
    def set_name(self):
        while True:
            name = input("Department name: ")
            if not name:
                print("Name cannot be empty.")
                continue
            if not name.isalpha():
                print("Name cannot contain numbers or symbols!")
                continue
            else:
                self.__name = name
                break

    def set_budget(self):
        while True:
            budget = input("Department annual budget: ")
            if not budget:
                print("Department cannot be empty or zero.")
                continue
            if not budget.isnumeric():
                print("Department cannot contain letters or symbols.")
                continue
            else:
                self.__budget = budget
                break

    def set_phone(self):
        while True:
            phone = input("Department phone: ")
            if not phone:
                print("Phone cannot be empty.")
                continue
            if not phone.isnumeric():
                print("Phone cannot contain letters or symbols.")
                continue
            if len(str(phone)) != 10:
                print("Phone must be 10 digits long.")
                continue
            else:
                self.__phone = phone
                break
    
    def get_name(self):
        return self.__name
    
    def get_budget(self):
        return self.__budget
    
    def get_phone(self):
        return self.__phone
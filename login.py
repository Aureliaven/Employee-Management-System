import datetime
import re

class Login:
    def __init__(self, user, password, access):
        self.__user = user
        self.__password = password
        self.__access = access
    
    def createUser(self):
        validUser = False
        validPassword = False
        while validUser == False or validPassword == False:
            user = input("\nUsername (must be letters only and no more than 16 characters long): ")
            password = input("\nPassword: ")
            try:
                if not re.search("^[A-Za-z]+$", user) and len(user) > 16:
                    print("Invalid username")
                elif len(password) < 7 or len(password) > 20:
                    print("Invalid password")
                else:
                    self.__user = user
                    self.__password = password
                    self.__access = "user"
                    validUser = True
                    validPassword = True
            except:
                print("something went wrong")

    def createAdmin(self):
        validUser = False
        validPassword = False
        while validUser == False or validPassword == False:
            user = input("\nUsername (must be letters only and no more than 16 characters long): ")
            password = input("\nPassword Enter (MINIMUM of eight characters, at least one uppercase letter, one lowercase letter and one number): ")
            try:
                if not re.search("^[A-Za-z]+$", user) and len(user) > 16:
                    print("Invalid username")
                elif not re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
                    print("Invalid password")
                else:
                    self.__user = user
                    self.__password = password
                    self.__access = "admin"
                    validUser = True
                    validPassword = True
            except:
                print("something went wrong")
            

    def userLogin(self):
        validAttempt = True
        counter = 0
        #today = datetime.datetime.today
        #nextvalidAttempt = datetime.datetime.today
        while validAttempt == True:
            user = input("\nUsername: ")
            password = input("\nPassword: ")

            if user != self.__user or password != self.__password:
                if counter >= 5: #and today == nextvalidAttempt:
                    print("Too many attempts!")
                    #nextvalidAttempt = today + datetime.timedelta(days=1)
                    validAttempt = False
                    return False
                #if counter >= 5 #and today < nextvalidAttempt:
                    #print("Too many attempts, please try again tomorrow!")
                    #return False
                
                print("\nIncorrect username or passowrd!")
                counter +=1
                
            elif user == self.__user and password == self.__password:
                print("login successful")
                return self.__access
            
    def get_user(self):
        return self.__user
    def get_password(self):
        return self.__password
    def get_access(self):
        return self.__access
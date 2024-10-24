import datetime
import hashlib

class User:
    
    def __init__(self, name = "", phone = "", email = "", password = "", age = 0, gender = ""):
        self.name = name
        self.phone = phone
        self.email = email
        self.password = password
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()
        
    def add_User_details(self):
        print("ENTER USER DETAILS: \n")
        self.name = input("Enter User's Name: ")
        self.phone = input("Enter User's phone: ")
        self.email =input("Enter User's Email: ")
        self.password =input("Enter User's Password: ").encode('utf-8')
        self.password = hashlib.sha256(self.password).hexdigest()
        self.age = int(input("Enter User's Age: "))
        self.gender =input("Enter User's Gender: ")
        
"""user = User()
user.add_User_details()
print(vars(user))"""
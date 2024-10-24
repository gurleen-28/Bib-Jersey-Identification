"""
    create table Customer(
        cid int primary key auto_increment,
        name varchar(256),
        phone varchar(15),
        email varchar(256),
        age int,
        gender varchar(10),
        created_on datetime
        
    );
    """
import datetime

class Customer:
    
    def __init__(self, cid=0, name="", phone="", email="", age=0, gender="", created_on=""):
        self.cid = cid
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.created_on = datetime.datetime.now()
        
    def add_Customer_details(self):
        print("ENTER Customer DETAILS: \n")
        self.name = input("Enter Customer's Name: ")
        self.phone = input("Enter Customer's phone: ")
        self.email =input("Enter Customer's Email: ")
        self.age = int(input("Enter Customer's Age: "))
        self.gender = input("Enter Customer's Gender: ")
        
    def update_Customer_details(self):
        name = input("Enter Customer's Name: ")
        if len(name)!=0:
            self.name = name
        
        phone = input("Enter Customer's phone: ")
        if len(phone)!=0:
            self.phone = phone
            
        email =input("Enter Customer's Email: ")
        if len(email)!=0:
            self.email = email
            
        age = (input("Enter Customer's Age: "))
        if len(age)!=0:
            self.age = int(age)
            
        gender = input("Enter Customer's Gender: ")
        if len(gender)!=0:
            self.gender = gender
        
        
    def show(self):
        print("********************CUSTOMER**********************")
        print("Name: {} | Phone: {} | ".format(self.name, self.phone))
        print("Email: {} | Age: {} | Gender: {}".format(self.email, self.age, self.gender)) 
        print("**********************************************************")
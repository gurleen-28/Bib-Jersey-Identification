"""
create table Patient(
        pid int primary key auto_increment,
        name varchar(256),
        phone varchar(15),
        problem_identified varchar(256),
        dob date,
        gender varchar(10),
        created_on datetime
        
    );
    """
    
import datetime

class Patient:
    
    def __init__(self, pid=0, name="", phone="", problem_identified="", dob=0, gender="", created_on=""):
        self.pid = pid
        self.name = name
        self.phone = phone
        self.problem_identified = problem_identified
        self.dob = dob
        self.gender = gender
        self.created_on = datetime.datetime.now()
        
    def add_Patient_details(self):
        print("ENTER PATIENT DETAILS: \n")
        self.name = input("Enter Patient's Name: ")
        self.phone = input("Enter Patient's phone: ")
        self.problem_identified =input("Enter Patient's Problem: ")
        self.dob = (input("Enter Patient's DOB(yyyy-mm-dd): "))
        self.gender = input("Enter Patient's Gender: ")
        
    def update_Patient_details(self):
        name = input("Enter Patient's Name: ")
        if len(name)!=0:
            self.name = name
        
        phone = input("Enter Patient's phone: ")
        if len(phone)!=0:
            self.phone = phone
            
        problem_identified =input("Enter Patient's problem: ")
        if len(problem_identified)!=0:
            self.problem_identified = problem_identified
            
        age = (input("Enter Patient's Age: "))
        if len(age)!=0:
            self.age = int(age)
            
        gender = input("Enter Patient's Gender: ")
        if len(gender)!=0:
            self.gender = gender
        
        
    def show(self):
        print("********************CUSTOMER**********************")
        print("Name: {} | Phone: {} | Created_on: {}".format(self.name, self.phone, self.created_on))
        print("Problem: {} | DOB: {} | Gender: {}".format(self.problem_identified, self.age, self.gender)) 
        print("**************************************************")
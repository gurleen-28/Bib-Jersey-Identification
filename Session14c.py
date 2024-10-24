"""
create table Consultation(
        cid int primary key auto_increment,
        pid int,
        remarks varchar(256),
        medicines varchar(256),
        next_followup datetime,
        created_on datetime,
        FOREIGN KEY (pid) REFERENCES Patient(pid)
    );
    """


import datetime

class Consultation:
    
    def __init__(self, cid=0, pid=0, remarks="", medicines="", next_followup=0, created_on=""):
        self.cid = cid
        self.pid = pid
        self.remarks = remarks
        self.medicines = medicines
        self.next_followup = next_followup
        self.created_on = datetime.datetime.now()
        
    def add_Consultation_details(self):
        print("ENTER CONSULTATION DETAILS: \n")
        self.pid = input("Enter Patient's ID: ")
        self.remarks = input("Enter Consulatation Remarks: ")
        self.medicines =input("Enter Medicines: ")
        self.next_followup = input("Enter next_followup(yyyy-mm-dd hh:mm:ss): ")
        
        
    def update_Consulatation_details(self):
        PId = input("Enter Patient's ID: ")
        if len(PId)!=0:
            self.PId = PId
        
        remarks = input("Enter Consulation Remarks: ")
        if len(remarks)!=0:
            self.remarks = remarks
            
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
        print("CID: {} | PID: {} | REMARKS: {}".format(self.cid, self.PId, self.remarks))
        print("MEDICINES: {} | NEXT_FOLLOWUP: {} | CREATED_ON: {}".format(self.medicines, self.next_followup, self.created_on)) 
        print("**************************************************")
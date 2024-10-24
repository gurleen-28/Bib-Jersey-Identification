from Session14 import Patient
from Session14a import Database
from Session14c import Consultation
from tabulate import tabulate

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO DOCTOR'S APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    db = Database()
    
    while True:
        print("1.Add New Patient")
        print("2.Update Existing Patient")
        print("3.View Existing Patient")
        print("4.View Patient by Phone")
        print("5.View Patient by PID")
        print("6.View All Patients")
        print("7.Add Consultation for Patient")
        print("8.View all Consultations")
        print("9.View Consultations of a Patient")
        print("10.View FollowUps")
        print("0. Quit App")
        
        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            patient = Patient()
            patient.add_Patient_details()
            sql = "insert into Patient values(null, '{name}', '{phone}', '{problem_identified}', '{dob}', '{gender}', '{created_on}')".format_map(vars(patient))
        
            db.write(sql)
            print("[PMS APP]",patient.name,"Saved in Database.")
            
            
        elif choice == 2:
            pid = (int(input("Enter Patient's ID to be Updated:  ")))
            sql = "Select * from Patient where pid ={}".format(pid)
            rows = db.read(sql)
            print(rows)
            patient = Patient(pid=rows[0][0], name=rows[0][1], phone=rows[0][2], problem_identified=rows[0][3], dob=rows[0][4], gender=rows[0][5])
            
            print("Patient to Update: ")
            patient.show()
            patient.update_Patient_details()
            sql = "update Patient set name = '{name}', phone='{phone}', problem_identified='{problem_identified}', dob={dob}, gender='{gender}', created_on='{created_on}' where pid = {pid}".format_map(vars(patient))

            db.write(sql)
            patient.show()
        
        elif choice == 3:
            pid = int(input("Enter Patient ID to be Deleted : "))
            
            sql = "delete from Patient where pid = {}".format(pid)
            ask = int(input("Are You Sure You want to Delete (Yes/No) : "))
            if ask == "yes":
                db.write(sql)
                print("[PMS APP]",pid,"Deleted from Database.")
            else:
                print("Delete Operation Skipped.")
        
        elif choice == 4:
            phone = (input("Enter Patient's Phone Number:  "))
            sql = "Select * from Patient where phone ='{}'".format(phone)
            rows = db.read(sql)
            
            columns = ["pid", "name", "phone", "problem_identified", "age", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
        
        elif choice == 5:
            pidid = (int(input("Enter Patient's ID:  ")))
            sql = "Select * from Patient where pid ={}".format(pid)
            rows = db.read(sql)
            
            columns = ["pid", "name", "phone", "problem_identified", "dob", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
        
        elif choice == 6:
            sql = "Select * from Patient"
            rows = db.read(sql)
            
            columns = ["pid", "name", "phone", "problem_identified", "dob", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
            
            #for row in rows:
               # print(row)
        
        elif choice == 0:
            break
        else:
            print("[PMS APP] Invalid Choice")
            
if __name__ == "__main__":
    main()
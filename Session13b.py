#CUSTOMER MANAGEMENT APP

from Session13 import Customer
from Session13a import Database
from tabulate import tabulate

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("WELCOME TO CUSTOMER MANAGEMENT APP")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    db = Database()
    
    while True:
        print("1.Add New Customer")
        print("2.Update Existing Customer")
        print("3.View Existing Customer")
        print("4.View Customer by Phone")
        print("5.View Customer by CID")
        print("6.View All Customers")
        print("0. Quit App")
        
        choice = int(input("Enter Your Choice : "))
        
        if choice == 1:
            customer = Customer()
            customer.add_Customer_details()
            print(vars(customer))
            sql = "insert into customer values(null, '{name}', '{phone}', '{email}', {age}, '{gender}', '{created_on}')".format_map(vars(customer))
        
            db.write(sql)
            print("[CMS APP]",customer.name,"Saved in Database.")
            
            
        elif choice == 2:
            cid = (int(input("Enter Customer's ID to be Updated:  ")))
            sql = "Select * from Customer where cid ={}".format(cid)
            rows = db.read(sql)
            print(rows)
            customer = Customer(cid=rows[0][0], name=rows[0][1], phone=rows[0][2], email=rows[0][3], age=rows[0][4], gender=rows[0][5])
            
            print("Customer to Update: ")
            customer.show()
            customer.update_Customer_details()
            sql = "update Customer set name = '{name}', phone='{phone}', email='{email}', age={age}, gender='{gender}', created_on='{created_on}' where cid = {cid}".format_map(vars(customer))

            db.write(sql)
            customer.show()
        
        elif choice == 3:
            cid = int(input("Enter Customer ID to be Deleted : "))
            
            sql = "delete from Customer where cid = {}".format(cid)
            ask = int(input("Are You Sure You want to Delete (Yes/No) : "))
            if ask == "yes":
                db.write(sql)
                print("[CMS APP]",cid,"Deleted from Database.")
            else:
                print("Delete Operation Skipped.")
        
        elif choice == 4:
            phone = (input("Enter Customer's Phone Number:  "))
            sql = "Select * from Customer where phone ='{}'".format(phone)
            rows = db.read(sql)
            
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
        
        elif choice == 5:
            cid = (int(input("Enter Customer's ID:  ")))
            sql = "Select * from Customer where cid ={}".format(cid)
            rows = db.read(sql)
            
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
        
        elif choice == 6:
            sql = "Select * from Customer"
            rows = db.read(sql)
            
            columns = ["cid", "name", "phone", "email", "age", "gender", "created_on"]
            print(tabulate(rows, headers = columns, tablefmt = 'grid'))
            
            #for row in rows:
               # print(row)
        
        elif choice == 0:
            break
        else:
            print("[CMS APP] Invalid Choice")
            
if __name__ == "__main__":
    main()


        
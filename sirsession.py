from sessionnew3 import Customer
from session23 import Database

def main():
    print("-------------------")
    print("WELCOME to CMS APP")
    print("-------------------")

    db = Database()

    while True:
        print("1: Add New Customer")
        print("2: Update Existing Customer")
        print("3: Delete Existing Customer")
        print("4: View Customer By Phone")
        print("5: View Customer By CID")
        print("6: View All Customers")
        print("0: To Quit App")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            customer = Customer()
            customer.add_Customer_details()
            sql = "insert into Customer values(null, '{name}', '{phone}', '{email}', {age}, '{gender}')".format_map(vars(customer))

            # sql = "insert into Customer values(null, '{}', '{}', '{}', {}, '{}', null)".format(customer.name, customer.phone, customer.email, customer.age, customer.gender)

            db.write(sql)
            print("[CMS App]", customer.name, "Saved in DataBase")

        elif choice == 2:
            pass
        elif choice == 3:
            cid = int(input("Enter Customer ID to be Deleted: "))
            sql = "delete from Customer where cid = {}".format(cid)
            db.write(sql)
            print("[CMS App]", cid, "Deleted from DataBase")
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 0:
            break
        else:
            print("[CMS APP] Invalid Choice", choice)


if __name__ == "__main__":
    main()
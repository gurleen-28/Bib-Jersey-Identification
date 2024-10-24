from Session9E import Customer

print("***************************************")
print("WELCOME TO CUSTOMER MANAGEMENT SYSTEM")
print("***************************************")

while True:
    print("1 : ADD CUSTOMER")
    print("2 : VIEW CUSTOMER")
    print("0 : QUIT")
    
    choice = input("ENTER THE CHOICE OF CUSTOMER : ")
    print("YOU SELECTED : ", choice)
    
    if choice == 1:
        file = open("customer.csv", "a")
        customer = Customer()
        customer.add_customer_details()
        customer.show()
        
        data = customer.to_csv()
        file.write(data)
        print("DATA WRITTEN : ", data)
        
    elif choice == 2:
        file = open("customer.csv", "r")
        lines = file.readlines()
        for line in lines:
            print(line)
            
    elif choice == 0:
        print("***************************************")
        print("THANK YOU")
        print("***************************************")
        file.close()
        break
        
    
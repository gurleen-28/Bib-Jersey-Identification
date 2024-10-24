from Session9E import Customer

print("*************************************")
print("WELCOME TO CUSTOMER MANAGEMENT SYSTEM")
print("*************************************")

file = open("customer.csv","a")

while True:
    
    print("1 : Add Customer")
    print("2 : View Customer")
    print("0 : Quit")

    choice = int(input("Enter Your Choice : "))
    print("You Selected : ", choice)


    if choice == 1:
        customer = Customer()
        customer.add_Customer_details()
        customer.show()
        
        data = customer.to_csv()
        file.write(data)
        print("DATA WRITTEN : ",data)
        
    elif choice == 2:
        file = open("customer.csv","r")
        
        
    elif choice == 0:
        print("*************************************")
        print("Thank you....")
        print("*************************************")
        file.close()
        break
        
    
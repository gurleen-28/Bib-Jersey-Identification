name = input("ENTER CUSTOMER NAME : ")
phone = input("ENTER CUSTOMER PHONE : ")
email = input("ENTER CUSTOMER EMAIL : ")

customer_details = " {} , {} , {}\n".format(name, phone, email)
file = open("customers.csv" , "a")
file.write(customer_details)
print("CUSTOMER DATA SAVED..")
file.close()
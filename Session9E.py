

class Customer:
    
    def __init__(self, name="NA", phone="NA", address="NA", age=20, gender="NA", email="NA"):
        self.name = name
        self.phone = phone
        self.address = address
        self.age = age
        self.gender = gender
        self.email = email
        
    def add_Customer_details(self):
        print("ENTER Customer DETAILS: \n")
        self.name = input("Enter Customer's Name: ")
        self.phone = input("Enter Customer's phone: ")
        self.address = input("Enter Customer's address: ")
        self.age = input("Enter Customer's age: ")
        self.gender = input("Enter Customer's Gender: ")
        self.email = input("Enter Customer's Email: ")
        
    def show(self):
        print("********************CUSTOMER**********************")
        print("Name: {} | Phone: {} | Address: {}".format(self.name, self.phone, self.address))
        print("Age: {} | Gender: {} | Email: {}".format(self.age, self.gender, self.email)) 
        print("**********************************************************")
        
    def to_csv(self):
        data = "{},{},{},{},{},{}\n.format(self.name, self.phone, self.address,self.age, self.gender, self.email)"
        return data
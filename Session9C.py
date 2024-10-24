from Session9B import Vehicle

class Driver:
    
    def __init__(self, name="NA", email="NA", gender="NA", age=20, phone="NA", vehicle=None, license_number="NA", rating=4.8):
        self.name = name
        self.email = email
        self.gender = gender
        self.age = age
        self.phone = phone
        self.license_number = license_number
        self.rating = rating
        self.vehicle = vehicle
    
    def add_Driver_details(self):
        print("ENTER DRIVER DETAILS: \n")
        self.name = input("Enter Driver's Name: ")
        self.email = input("Enter Driver's email: ")
        self.gender = input("Enter Driver's gender: ")
        self.age = input("Enter Driver's age: ")
        self.phone = input("Enter Driver's phone: ")
        self.license_number = input("Enter Driver's license_number: ")
        self.rating = input("Enter Driver's rating: ")
        self.vehicle = Vehicle()
        self.vehicle.add_Vehicle_details()
       

        
        
    def show(self):
        print("*************************DRIVER*********************************")
        print("Name: {} | Email: {} | Gender: {}".format(self.name, self.email, self.gender))
        print("Age: {} | Phone: {} | License Number: {}".format(self.age, self.phone, self.license_number))  
        print("Ratings: {}".format(self.rating))
        print("**********************************************************")
        
        self.vehicle.show()
        
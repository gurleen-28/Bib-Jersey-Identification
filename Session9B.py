"""
Driver has a vehicle
Customer can book ride

Identify objects and classes in this

Driver = name, email, gender, age, phone, vehicle, license_number, rating
   1 Driver has 1 Vehicle
Vehicle = brand, model, registration_number, color
Customer = name, phone, address, age, gender, email
Ride = customer, date, time, distance, fare, driver, from_location, to_location
   1 Ride has 1 Customer
   1 Ride has 1 Driver

"""

class Vehicle:
    
    def __init__(self, brand ="NA" , model ="NA", registration_number ="NA", color = "White"):
        self.registration_number = registration_number
        self.brand = brand
        self.model = model
        self.color = color
    
    def add_Vehicle_details(self):
        print("ENTER VEHICLE DETAILS: \n")
        self.registration_number = input("Enter Vehicle Registration number: ")
        self.brand = input("Enter Vehicle Brand: ")
        self.model = input("Enter Vehicle Model: ")
        self.color = input("Enter Vehicle Color: ")
        
    def show(self):
        print("*************************VEHICLE*********************************")
        print("Registration number: {} | Brand: {}".format(self.registration_number, self.brand))  
        print("Model: {} | Color: {}".format(self.model, self.color))  
        print("**********************************************************")
        
#vehicle = Vehicle()
#vehicle.add_Vehicle_details()
#vehicle.show()
        


        
from Session9E import Customer
from Session9C import Driver
from Session9B import Vehicle

class Ride :
    
    def __init__(self, customer = None, date = "20th June, 2024 ",time = "12:00", distance = 8, fare = 230, driver = None, from_location = "Home", to_location = "Work" ) :
        print("ENTER RIDE DETAILS: \n")
        self.customer = customer
        self.date = date
        self.time = time
        self.distance = distance
        self.fare = fare
        self.driver = driver
        self.from_location = from_location
        self.to_location = to_location
        
    def add_Ride_details(self):
        print("ENTER RIDE DETAILS: \n")
        self.from_location= input("Enter from location: ")
        self.to_location = input("Enter to location: ")
    
    def link_customer(self, customer):
        self.customer = customer
    
    def link_driver(self, driver):
        self.driver = driver
           
    def show(self):
        
        self.customer.show()
        
        print("********************RIDE**********************")
        print("From: {} | To: {} | Distance: {}".format(self.from_location, self.to_location, self.distance))
        print("Fare: {} | Date: {} | Time: {}".format(self.fare, self.date, self.time)) 
        print("**********************************************************")
        
        self.driver.show()
        
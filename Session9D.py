from Session9E import Customer
from Session9C import Driver
from Session9F import Ride
from Session9B import Vehicle


driver = Driver()
driver.add_Driver_details()

customer = Customer()
customer.add_Customer_details()

ride = Ride()
ride.add_Ride_details()
ride.link_customer(customer)
ride.link_driver(driver)

print("RIDE BOOKED...")
ride.show()




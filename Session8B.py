from Session8 import Dish
from Session8A import Menu

class Restaurant:
    
    def __init__(self,  name, phone, email, address, operating_hours, ratings, menu):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        self.operating_hourse = operating_hours
        self.ratings = ratings
        self.menu = menu
        
    def show(self):
        print("RESTAURANT")
        print("Restaurant:{} | {} | {}".format(self.name, self.phone, self.email))
      
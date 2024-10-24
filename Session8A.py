#from Session8 import Dish

class Menu:
    def __init__(self, name="NA", number_of_dishes=0, menu_dishes=[]):
        print("SELF IS:",self)
        self.name = name
        self.number_of_dishes = number_of_dishes
        self.menu_dishes = menu_dishes
        
    def show(self):
        print("**********************************************")
        print("Menu:{} | {} ".format(self.name, self.number_of_dishes ))
        print("**********************************************\n")
        
        print("Dishes:")
        for idx in range(len(self.menu_dishes)):
            self.menu_dishes[idx].show()
              
"""dishes = [
     Dish(),
     Dish(name="Coffee", price=200, rating=5),
     Dish("Bread", 180, 4.8)
    ]

menu = Menu (
    name = "Indian Veggie Delight",
    number_of_dishes = len(dishes),
    menu_dishes = dishes
    )

menu.show()
"""
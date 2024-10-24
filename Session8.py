"""
1.Dish : name, price, rating
2.Menu : name, number_of_dishes, dishes
    1 Menu can have many dishes
3.Restaurant : name, phone, email, address, operating_hours, ratings, menu
    1 Restaurant can have 1 menu
    """
    
class Dish:
    def __init__(self, name="NA", price=0, rating=1.5):
        print("SELF IS:",self)
        self.name = name
        self.price = price
        self.rating = rating
        
    def show(self):
        print("**********************************************")
        print("Dish:{} | {} | {}".format(self.name, self.price, self.rating ))
        print("**********************************************\n")
           
# dish1 = Dish()
#print("dish1:",hex(id(dish1)))

# dish2 = Dish(name="Coffee", price=200, rating=5)
# #print("dish2:",hex(id(dish2)))

# dish3 = Dish("Bread", 180, 4.8)
#print("dish3:",hex(id(dish3)))

#dish1.show()
#dish2.show()
#dish3.show()
dishes = [
    Dish(),
    Dish(name="Coffee", price=200, rating=5),
    Dish("Bread", 180, 4.8)
    
]

print("DISHES:\n")
for idx in range(len(dishes)):
    dishes[idx].show()
        
        
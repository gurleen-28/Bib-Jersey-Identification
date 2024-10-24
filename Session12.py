"""create table customer(
    cid int primary key auto_increment,
    name varchar(256),
    phone varchar(15),
    email varchar(256),
    age int,
    gender varchar(10)
)"""

class Customer:
    
    def __init__(self, name, phone, email, age, gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        
customer1 = Customer(name = "John", phone = "+91 98765 12345", email = "john@abc.com", age = 20, gender = "male")

print(vars(customer1))
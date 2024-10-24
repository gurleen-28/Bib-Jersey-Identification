#Properties
"""
Indexing
Negative Indexing
Slicing
Concatenation
Multiplicity
Membership Testing
"""

quote = "Search the Candle rather than Cursing the Darkness"
print("1. Hashcode of quote : ", id(quote))

print(quote[0])
print(quote[-1])
print(quote[-8:])

quote = quote + "\n" + "Be Expectional\n"
print(quote)
print("2. Hashcode of quote : ", id(quote))

print("````````````````````````````````")
data = quote * 3
print(data)
print("````````````````````````````````")

print("the" in quote)

email = input("Enter your Email : ")
if "@" in email and "." in email:
    print("Email is well formed:", email)
else:
    print("Email is not well formed:", email) 
    
contacts = ["john", "jennie", "kia", "joe", "jackson", "anna", "sia"]
search = input("Enter your Keyword : ")
for contact in contacts:
    if search in contact:
        print(contact)
password = "  Helloooo  "
print("Password : ", len(password))
#strip is used to remove blank spaces before and after the string or characters
p1 = password.strip()
print(p1, len(p1))

data = "000035490000"
print(data.strip("0"))
print(data)

amount = 35.490000
new_amount = float(str(amount).strip("0"))
print(new_amount, type(new_amount))

quote = "Search the Candle rather than Cursing the Darkness"
s1 = quote.replace("the", "hiiiiiiiiiiiiiiiiiiiiiiiiii")
print(quote)
print(s1)

message = "No Internet Connection"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

amount = 545
data = str(amount).zfill(8)
print("Data is : ", data)

quote = "Search the Candle rather than Cursing the Darkness"
idx1 = quote.find("the")
idx2 = quote.find("dark")
print("idx is : ", idx1)

print(quote[idx1:idx1+4])
print(quote[idx2:])

idx3 = quote.rfind("the")
print(idx3)

print(quote.index("the"))
print(quote.rindex("the"))



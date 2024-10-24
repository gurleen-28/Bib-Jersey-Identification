#arithmetic operators
#assignment operators
#==,+=,-=,*=,**=,/=,//=,%=
#conditinal operators
#==,!=,<,>=,<=

cab_fare=500
e_wallet=200

result= cab_fare>e_wallet

print("can i book the cab:",result)
print(type(result))

email=input("enter email:")
password=input("enter password:")

print("is login success?")
result= (email=="john@example.com") and (password=="john123")
print(result)

#membership testing
#is,is not
a=10
b=10

print(a==b)
print(a is b)
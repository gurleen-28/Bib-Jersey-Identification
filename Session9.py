def add(num1 , num2):
    result = num1 + num2
    print("Result is: {}".format(result))
    
print(hex(id(add)))
print("Add is:",add)#add is a fxn and we weill see hashcode of fxn

add(10 , 20)

hello = add
hello(11 , 22)

#if you redefine the same fxn , the previous fxn will be removed from the memory and new definition will exist
def add(num1 , num2 , num3):
    result = num1 + num2 + num3 + 10
    print("Result is: {}".format(result))
    
print(hex(id(add)))
print("Add is:",add)#add is a fxn and we weill see hashcode of fxn

add(10 , 20 , 30)
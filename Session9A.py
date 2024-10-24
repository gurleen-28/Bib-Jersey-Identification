def add(num1 , num2 , num3):
    result = num1 + num2 + num3 
    print("Result is: {}".format(result))
    
#add(10 , 20, 30)
add(num1 = 10 , num3 = 20 , num2 = 30)

#Default arguments
def square(num = 5):
    result = num * num
    print("Result is: {}".format(result))
    
square()
square(3)
square(num=9)

#def subtract(num1 = 10 , num2):#error as it works from right to left as if we will give value to left num we need to pass value to right one as well but it is not the case when we will pass value to right num;it will work
def subtract(num1 , num2 = 10):
    result = num1 -  num2
    print("Result is: {}".format(result))
    
subtract(num1 = 10)
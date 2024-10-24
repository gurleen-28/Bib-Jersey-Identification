num1=10
num2=8

print("num1 in binary is:  ",bin(num1))
print("num2 in binary is:  ",bin(num2))

result1=num1&num2#and
result2=num1|num2#or
result3=num1^num2#xor

print("result1:",result1)
print("result2:",result2)
print("result3:",result3)

#shift operators
#>>,<<

num1=8
num2=2

result=num1>>num2#8//2power2
print("result rigjt shift is:",result)

result2=num1<<num2#8*2power2
print("result rigjt shift is:",result2)

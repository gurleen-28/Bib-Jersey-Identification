#Nested Loops

for i in range(0,8):
    #print(i%2)
    
    for j in range(0,8):
        j=j+i
        print(j%2,end="   ")
        
    print()
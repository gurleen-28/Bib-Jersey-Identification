black_square="\u25A1"
white_square="\u25A0"

print(black_square)
print(white_square)

for i in range(0,8):
    #print(i%2)
   
    
    for j in range(0,8):
        if i%2==0:
           if j%2==0:
             print(black_square,end="  ")  
           else:
             print(white_square,end="  ")     
        else:
            if(j+1)%2==0:
                print(black_square,end="  ")  
            else:
                print(white_square,end="  ")   
        
    print()

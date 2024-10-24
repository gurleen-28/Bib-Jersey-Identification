#loops
#ELEVATOR PROBLEM
floors=10
floor=0

floor_to_go=input("Enter the Floor You want to reach:")
while floor<=floors:
    print("AT FLOOR:",floor)
    
    if floor_to_go==floor:
         print("You have reached your destination...",floor)
         break
    else:
        floor+=1
    
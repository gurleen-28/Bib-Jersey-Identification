promo_code=input("Enter your Promo Code:")
amount=float(input("Enter your Amount:"))

if promo_code=="ZOMATO":
    print("Promo Code can be applied.")
    
    if amount>300:
        discount=0.20*amount
        print("Dicount applied.")
        


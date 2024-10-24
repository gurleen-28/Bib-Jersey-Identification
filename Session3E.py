#promo code: ZOMATO
#condition1:more than 249
#condition2:50% off upto 150

amount=float(input("ENTER THE AMOUNT:"))
promo_code=input("ENTER YOUR COUPON:")

if promo_code=="ZOMATO":
    print("Promo code valid")
    
    if amount>249:
        print("PROMO CODE APPLIED...")
        discount=0.50*amount
        amount-=discount
        print("Discount is:",amount)
        print("Amount to be paid: ",amount)
    else:
        print("Amount is Low..")
else:
   print("Promo Code Invalid..")
#you can apply promo code if and only if min amount is 500
promo_code="GET200"
min_amount=500

amount=float(input("Enter your amount:  "))

if amount>min_amount:
    print("You can apply the promo code",promo_code)
else:
    print("You cannot apply the promo code",promo_code)
    print("Add items worth: ",(min_amount-amount),"..more")
    
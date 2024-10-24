"""
    Principle of OOPS:
    1.Think of an Object
    
    instagram:views,comments,likes,saveReel,text,toLocation,fromLocation,passwordChange,Updation,DateofBirth,name,email
   
    2.Create a Class
    
    3.Create real object from class in memory
    """
    
class instagram:
    pass

reel=instagram()
#reel is a reference variable and instagram is a empty object
print(reel)

#Operations on object
#1.Write Operation
reel.name="Gurleen"
reel.dateofBirth="28 October,2003"
reel.email="gurleenn28@gmail.com"
reel.views=668
reel.comments=99
reel.likes="77k"

reel1=instagram()
reel1.name="Gurleen"
reel1.dateofBirth="28 October,2003"
reel1.email="gurleenn28@gmail.com"
reel1.views=1000
reel1.comments=69
reel1.likes="254k"

#2.Update Operation
reel.comments=78
reel.likes="990k"

#3.Read Operation
print("REEL'S DATA:")
print(vars(reel))#vars ia a inbuilt variable in python

#4.Delete Operation
del reel.views
print("REEL'S DATA AFTER DELETION:")
print(vars(reel))

reel2=reel
print("REEL'S DATA:")
print(vars(reel2))


    
    
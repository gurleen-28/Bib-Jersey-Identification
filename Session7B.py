class  instagram:
    #default constructor in python(__init__)
    def __init__(self):#this reel can be anything 
        print("SELF:",self)
        self.name="Gurleen"
        self.dateofBirth="28 October,2003"
        self.email="gurleenn28@gmail.com"
        self.views=668
        self.comments=99
        self.likes="77k"
        
reel=instagram()
print("REEL:",reel)
print("REEL DATA:")
print(vars(reel))   

reel1=instagram()  
print("REEL1:",reel)
print("REEL1 DATA:")
print(vars(reel1))      
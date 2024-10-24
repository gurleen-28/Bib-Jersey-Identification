"""quote1 = "Search the Candle rather then cursing the darkness\n"
quote2 = "Be Exceptional\n"

file = open("quotes.txt" , "a")
file.write(quote1)
file.write(quote2)

file.close()
print("THE DATA YOU HAVE WRITTEN IS.............")
"""

quote1 = input("ENTER THE QUOTE : ")
quote2 = input("\nALWAYS BE HPAENTER THE QUOTE : ")

file = open("quotes.txt" , "w")
file.write(quote1)
file.write(quote2)

file.close()
print("THE DATA YOU HAVE WRITTEN IS.............")


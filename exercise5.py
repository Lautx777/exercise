#Listas:
#Crea una lista con al menos cinco elementos y accede al tercer elemento.

#AGREGARLE MULTI-NIVELES, UNA LISTA CON LISTITAS ADENTRO
class Article():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
        
    def data(self):    
        print(f"Name: {self.__name}, Price:{self.__price} ")
        

coffe = Article("Coffe", 10) 
books = Article("Books", 20)
mountains = Article("Mountains", 30)
music = Article("Music", 40)
sunsets = Article("Sunsets", 50) 

        
my_list2 = [coffe,books,mountains,music,sunsets]

for article in my_list2:
    article.data()




#my_list = ["Coffe", "Books", "Mountains", "Music", "Sunsets", True] 

#print ("Complete List:")
#print("")
#print(my_list)

#print("")

#print(f"Value number 3 of the list:")
#print("")
#print(my_list[2])

#Se puede tener una lista de listas 
#Meter una lista de clases
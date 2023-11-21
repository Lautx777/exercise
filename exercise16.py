#Clases y Objetos:
#Crea una clase llamada "Car" con atributos "brand" y "model" y un método que imprima la información del automóvil.


class Car:
    def __init__(self, brand:str, model:int):
        self.__brand = brand
        self.__model = model
    
    def info(self):
        print(f"the car is brand {self.__brand}, and its model is the year {self.__model}.") 
        
car = Car("Audi", 1990)
car.info()
    


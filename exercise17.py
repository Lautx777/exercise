#Herencia:
#Crea una clase "SportsCar" que herede de la clase "Car" y tenga un atributo adicional "top_speed".

class Car:
    def __init__(self, brand:str, model:int):
        self.__brand = brand
        self.__model = model
    
    def info(self):
        print(f"the car is brand {self.__brand}, and its model is the year {self.__model}.") 
        
class Sports_Cars(Car):
    def __init__(self, brand: str, model: int, top_speed:int):
        super().__init__(brand, model)
        self.__top_speed = top_speed
        
    def info(self):
        super().info()
        print(f"Its top speed is {self.__top_speed} km/h.")
    

        
car = Car("Audi", 1990)
car.info()

car_sport = Sports_Cars("Mercedes", 2015, 120)
car_sport.info()
    


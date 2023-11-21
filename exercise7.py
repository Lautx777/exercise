#Funciones:
#Define una función que sume dos números y devuelve el resultado.


def sum(number1:float, number2:float) -> float:
    return number1 + number2
    
    
    
valor1:float = 20
valor2:float = 20    
suma:float = sum(valor1, valor2)
print(f"the sum of the {valor1} and {valor2} is: {suma}") 
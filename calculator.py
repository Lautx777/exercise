# calculator.py
#Manejo de Módulos de creación propia:
#Crea un módulo llamado calculator que contiene funciones para suma, resta, multiplicación y división.


def addition(a:float, b:float) -> float:
    return a + b

def subtraction(a:float, b:float) -> float:
    return a - b

def multiplication(a:float, b:float) -> float:
    return a * b

def division(a, b) -> float:
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: División por cero no permitida"

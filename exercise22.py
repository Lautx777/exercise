#Uso de Generadores:
#Crea un generador que genere números pares del 0 al 10.


def generator(max_value):
    number = 0
    while number < max_value:
        yield number
        number += 2

max_value = 10
for number in generator(max_value):
    print(number)

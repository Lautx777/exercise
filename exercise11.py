#Manejo de Errores (try-except):
#Utiliza try-except para manejar una excepción al intentar convertir una cadena a entero.
#runtime error 
#https://www.youtube.com/watch?v=IFfdRY609Fg

#Trying to convert a string to an integer
string = "123abc"

try:
    number = int(string)
    print("Conversion successful. The number is:", number)
except ValueError:
    print("Error: Couldn't convert the string to an integer. Make sure the string contains only digits.")

finally: print("you can always see me")

#Entender y segmentar posibles errores 
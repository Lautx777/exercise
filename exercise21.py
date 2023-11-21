#Manejo de Archivos JSON:
#Lee un archivo JSON llamado data.json, modifica un valor y luego guárdalo nuevamente.
import json


# Paso 1: Leer el archivo JSON
with open('exercise21.json', 'r') as archivo:
    datos = json.load(archivo)

# Paso 2: Modificar el valor deseado
datos['age'] = 30  # Modificamos la edad, por ejemplo

# Paso 3: Guardar los cambios en el archivo JSON
with open('exercise21.json', 'w') as archivo:
    json.dump(datos, archivo, indent=2)

print("¡Archivo modificado y guardado correctamente!")

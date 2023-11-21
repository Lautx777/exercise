#Lee un archivo de texto llamado example.txt y muestra su contenido. Luego, escribe algo en el archivo.
#https://www.freecodecamp.org/espanol/news/lectura-y-escritura-de-archivos-en-python-como-crear-leer-y-escribir-archivos/
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:                                                   #Crear el archivo en caso de que no exista    
    print("The file does not exist. Creating it...")
    with open('example.txt', 'w') as file:
        file.write("This is the initial content of the file.")
    print("File created. You can run the code again to see its content.")
    
                                                                          
    with open('example.txt', 'a') as file:                                  #Añadir texto al archivo
        file.write("\nThis is new content added to the end of the file.")


#Manejo de Fechas y Tiempo:
#Importa el módulo datetime y crea una función que devuelva la fecha y hora actual formateada como "YYYY-MM-DD HH:MM:SS".
#https://pythondiario.com/2014/05/obtener-fecha-y-hora-actual-en-python.html#google_vignette

from datetime import datetime

def date_time():
    current_date_time = datetime.now()

    formatted_date_time = current_date_time.strftime("%Y-%m-%d %H:%M:%S")
    #%Y - Numero de año entero (2014)
    #%m - Mes en número
    #%d - Día del mes
    #%H - Hora (formato 24 horas)
    #%M- Minutos
    #%S - Segundos
    
    return formatted_date_time

result = date_time()
print("Fecha y Hora Actual:", result)
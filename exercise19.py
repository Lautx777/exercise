#Manejo de Excepciones Personalizado:
#Define una excepción personalizada llamada "CustomError" y levántala en un bloque try-except.
#https://www.delftstack.com/es/howto/python/python-custom-exception/#google_vignette

class CustomError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


message = "Exception Triggered! Something went wrong."
raise CustomError(message)
        

import random # Importamos el módulo random de Python
from prueba_mongo import instanciar, consultar  # Asegúrate de que el nombre del módulo sea el correcto

def frotar(n_frases):
    # Llamamos a la función instanciar para obtener cliente_mongo y frases_auspiciosas
    cliente_mongo, frases_auspiciosas = instanciar()

    # Esta función devuelve una lista con n_frases auspiciosas, elegidas al azar de la base de datos de MongoDB
    frases = []  # Creamos una lista vacía para almacenar las frases
    docs = consultar(n_frases, frases_auspiciosas)  # Obtenemos los documentos con frases auspiciosas de la base de datos
    for doc in docs:  # Recorremos cada documento
        frase = doc["frase"]  # Obtenemos la frase del documento
        frases.append(frase)  # Añadimos la frase a la lista
    respuesta = []  # Creamos una lista vacía para almacenar la respuesta
    for i in range(n_frases):  # Repetimos n_frases veces
        frase = random.choice(frases)  # Elegimos una frase al azar de la lista
        respuesta.append(frase)  # Añadimos la frase a la respuesta

    # Cerrar la conexión después de usarla
    cliente_mongo.close()

    return respuesta  # Devolvemos la respuesta

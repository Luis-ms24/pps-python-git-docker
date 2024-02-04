from pymongo import MongoClient

def instanciar():
    # Conexión con el motor de MongoDB
    cliente_mongo = MongoClient('mongodb://mongo:27017/')
    
    # Conexión con la base de datos (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la colección (llamada colección en MongoDB)
    frases_auspiciosas = bd['frases_auspiciosas']
    
    return cliente_mongo, frases_auspiciosas

def inicializar(datos, frases_auspiciosas):
    # Comprobamos que no se haya inicializado previamente
    if frases_auspiciosas.count_documents({}) == 0:
        # Inserción de datos
        frases_auspiciosas.insert_many(datos)

def consultar(n_frases, frases_auspiciosas):
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    if not frases_aleatorias:
        print("No se encontraron frases auspiciosas.")
        return []
    
    # Imprimir las frases
    for frase in frases_aleatorias:
        print(frase['frase'])
    return frases_aleatorias

def cerrar_conexion(cliente_mongo):
    # Cerrar cliente de MongoDB
    cliente_mongo.close()

if __name__ == "__main__":
    datos = [
        {"frase": "El éxito es como un fantasma, muchos hablan de él, pero pocos lo han visto de verdad"},
        # ... Otras frases ...
    ]

    # Instanciar
    cliente_mongo, frases_auspiciosas = instanciar()

    # Inicializar (opcional, si la colección está vacía)
    inicializar(datos, frases_auspiciosas)

    # Consultar
    n_frases = 3
    consultar(n_frases, frases_auspiciosas)

    # Cerrar conexión
    cerrar_conexion(cliente_mongo)

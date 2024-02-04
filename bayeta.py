import random # Importamos el módulo random de Python

def frotar(n_frases: int = 1) -> list():
 
    frases = [] # Creamos una lista vacía donde guardaremos las frases generadas
    with open("frases.txt", "r") as f: # Abrimos el fichero de texto que contiene las frases posibles, en modo lectura
        frases_posibles = f.read().splitlines() # Leemos el contenido del fichero y lo dividimos por líneas, guardando cada frase en una lista
    frases = random.sample(frases_posibles, n_frases) # Elegimos N frases al azar de la lista de frases, sin repetición, y las guardamos en la lista de frases
    return frases # Devolvemos la lista de frases

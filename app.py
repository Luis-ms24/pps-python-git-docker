from bayeta import frotar # Importamos la función frotar del fichero bayeta.py

n = 3 # Elegimos el número de frases que queremos obtener
frases = frotar(n) # Llamamos a la función frotar con el número de frases y guardamos la lista de frases que nos devuelve

for frase in frases: # Recorremos la lista de frases
    print(frase) # Imprimimos cada frase por la salida estándar

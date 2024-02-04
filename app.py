from flask import Flask, jsonify # Importamos la función jsonify del módulo flask, que nos permite convertir objetos de Python en JSON
from bayeta import frotar # Importamos la función frotar del fichero bayeta.py

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Hola, mundo'

@app.route('/frotar/<int:n_frases>') # Definimos una ruta para el endpoint GET /frotar/<n_frases>, usando el decorador app.route. Indicamos que el parámetro n_frases es de tipo entero
def frotar_bayeta(n_frases): # Definimos una función que se ejecutará cuando se acceda a la ruta, recibiendo el parámetro n_frases
    frases = frotar(n_frases) # Llamamos a la función frotar con el parámetro n_frases y guardamos la lista de frases que nos devuelve
    return jsonify(frases) # Devolvemos la lista de frases convertida en JSON como respuesta

""" if __name__ == '__main__': # Comprobamos si el fichero se ejecuta como programa principal
    app.run(debug=True, port=5000) # Ejecutamos la aplicación en modo depuración, que nos permite ver los errores y recargar la aplicación automáticamente cuando haya cambios
 """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
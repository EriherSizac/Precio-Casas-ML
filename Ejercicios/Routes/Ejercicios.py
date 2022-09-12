"""

"""
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os
import json
import numpy as np
from flask import Blueprint
from Global.utils.models import MODELO_EJERCICIOS
EJERCICIOS_BLUEPRINT = Blueprint('EJERCICIOS_BLUEPRINT',__name__)

@EJERCICIOS_BLUEPRINT.route("/formulario", methods=['GET'])
def formulario():
    return render_template('pagina.html')


# Envio de datos a través de Archivos
@EJERCICIOS_BLUEPRINT.route('/modeloFile', methods=['POST'])
def modeloFile():
    f = request.files['file']
    filename = secure_filename(f.filename)
    path = os.path.join(os.getcwd(), 'files', filename)
    f.save(path)
    file = open(path, "r")

    for x in file:
        info = x.split()
    print(info)
    datosEntrada = np.array([
        float(info[0]),
        float(info[1]),
        float(info[2])
    ])
    # Utilizar el modelo
    resultado = MODELO_EJERCICIOS.predict(datosEntrada.reshape(1, -1))
    # Regresar la salida del modelo
    return jsonify({"Resultado": str(resultado[0])})


# Envio de datos a través de Forms
@EJERCICIOS_BLUEPRINT.route('/modeloForm', methods=['POST'])
def modeloForm():
    # Procesar datos de entrada
    contenido = request.form

    datosEntrada = np.array([
        contenido['HP'],
        contenido['CS'],
        contenido['DESTINATION'],
        contenido['AGE'],
        contenido['VIP'],
        contenido['RS'],
        contenido['FC'],
        contenido['SM'],
        contenido['SPA'],
        contenido['VR']
    ])
    # Utilizar el modelo
    resultado = MODELO_EJERCICIOS.predict(datosEntrada.reshape(1, -1))
    # Regresar la salida del modelo
    return jsonify({"Resultado": str(resultado[0])})


# Envio de datos a través de JSON
@EJERCICIOS_BLUEPRINT.route('/modelo', methods=['POST'])
def modelo():
    # Procesar datos de entrada
    contenido = json.loads(request.data)
    print(contenido)
    datosEntrada = np.array([
        contenido['pH'],
        contenido['sulphates'],
        contenido['alcohol']
    ])
    # Utilizar el modelo
    resultado = MODELO_EJERCICIOS.predict(datosEntrada.reshape(1, -1))
    # Regresar la salida del modelo
    return jsonify({"Resultado": str(resultado[0])})

@EJERCICIOS_BLUEPRINT.route('/test', methods=['POST'])
def test():
    import datetime
    # Procesar datos de entrada
    contenido = request.json

    contenido['hora'] = str(datetime.datetime.now())
    print(contenido)
    # Regresar la salida del modelo
    return jsonify(contenido)
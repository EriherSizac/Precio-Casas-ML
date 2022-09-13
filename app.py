from flask import Flask, request, jsonify, render_template
from Global.utils.db import get, post
from dotenv import load_dotenv


# Inicializar el servidor
app = Flask(__name__)

# Cargar las variables de entorno
load_dotenv()

# Cargamos los blueprints
from Ejercicios.Routes.Ejercicios import EJERCICIOS_BLUEPRINT
from spaceship_titanic.Routes.Prediction import SPACESHIP_PREDICTIONS_BLUEPRINT


@app.route('/', methods=['GET'])
def root():
    return 'Hi'

# Registramos las blueprints
app.register_blueprint(EJERCICIOS_BLUEPRINT, url_prefix='/ejercicios')
app.register_blueprint(SPACESHIP_PREDICTIONS_BLUEPRINT, url_prefix='/spaceship')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')
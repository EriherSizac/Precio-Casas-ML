from flask import Flask, request, jsonify, render_template
from Global.utils.db import get, post
from dotenv import load_dotenv
from flask_mail import Mail
import os

# Inicializar el servidor
app = Flask(__name__)
# Inicializamos el cliente de Mail
mail = Mail()

# Cargar las variables de entorno
load_dotenv()

# Cargamos los blueprints
from Ejercicios.Routes.Ejercicios import EJERCICIOS_BLUEPRINT
from spaceship_titanic.Routes.Model import SPACESHIP_PREDICTIONS_BLUEPRINT


@app.route('/', methods=['GET'])
def root():
    return 'Hi'

# Registramos las blueprints
app.register_blueprint(EJERCICIOS_BLUEPRINT, url_prefix='/ejercicios')
app.register_blueprint(SPACESHIP_PREDICTIONS_BLUEPRINT, url_prefix='/spaceship')

# Configuramos la app con los datos del env
app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER')
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT')
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_USE_SSL')
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
mail.init_app(app)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port='8080')
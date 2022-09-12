"""

"""
from flask import Blueprint
from spaceship_titanic.Controllers.Prediction import *
SPACESHIP_PREDICTIONS_BLUEPRINT = Blueprint('SPACESHIP_PREDICTIONS', __name__)
@SPACESHIP_PREDICTIONS_BLUEPRINT.route('/getPrediction', methods=['GET'])
def cGetPrediction():
    return getPrediction()
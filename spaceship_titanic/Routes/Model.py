"""

"""
from flask import Blueprint
from spaceship_titanic.Controllers.Model import *
SPACESHIP_PREDICTIONS_BLUEPRINT = Blueprint('SPACESHIP_PREDICTIONS', __name__)
@SPACESHIP_PREDICTIONS_BLUEPRINT.route('/getPrediction', methods=['POST'])
def cGetPrediction():
    return getPrediction()

@SPACESHIP_PREDICTIONS_BLUEPRINT.route('/howToSurvive', methods=['POST'])
def cHowToSurvive():
    return howToSurvive()

@SPACESHIP_PREDICTIONS_BLUEPRINT.route('/info', methods=['GET'])
def cGetInfo():
    return getInfo()


@SPACESHIP_PREDICTIONS_BLUEPRINT.route('/hi', methods=['POST'])
def hi():
    return "Hi"

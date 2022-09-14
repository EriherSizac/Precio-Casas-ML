"""

"""
from spaceship_titanic.Classes.Prediction import Prediction
from flask import request, jsonify
import numpy as np
from Global.utils.models import ADABOOST
def getPrediction():
    json = request.json
    # Utilizar el modelo
    prediction = Prediction(json)
    res = {
        'Transported': bool(prediction.transported)
    }
    return res
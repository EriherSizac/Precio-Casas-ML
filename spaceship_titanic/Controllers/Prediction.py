"""

"""
from spaceship_titanic.Classes.Prediction import Prediction
from flask import request, jsonify
import numpy as np
from Global.utils.models import ADABOOST
def getPrediction():
    json = request.json
    print(info)
    """
    Index(['cryo_sleep', 'age', 'vip', 'room_service', 'food_court',
       'shopping_mall', 'spa', 'vr_deck', 'transported', 'passenger_group', 
       'Earth', 'Europa', 'Mars', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'P',
       'S', '55 Cancri e', 'PSO J318.5-22', 'TRAPPIST-1e'],
      dtype='object')"""

    # Utilizar el modelo
    prediction = Prediction(json)
    return prediction
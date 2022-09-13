"""

"""
from spaceship_titanic.Classes.Prediction import Prediction
from flask import request, jsonify
import numpy as np
from Global.utils.models import ADABOOST
def getPrediction():
    json = request.json
    info = list(json["form_data"].values())
    print(info)
    params = [json["name"],json["email"],json["phone"],json["age"],json["country"]]
    """
    Index(['cryo_sleep', 'age', 'vip', 'room_service', 'food_court',
       'shopping_mall', 'spa', 'vr_deck', 'transported', 'passenger_group', 
       'Earth', 'Europa', 'Mars', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'P',
       'S', '55 Cancri e', 'PSO J318.5-22', 'TRAPPIST-1e'],
      dtype='object')"""

    datosEntrada = np.array([
        float(info[0]),
        float(info[1]),
        float(info[2]),
        float(info[3]),
        float(info[4]),
        float(info[5]),
        float(info[6]),
        float(info[7]),
        float(info[8]),
        float(info[9]),
        float(info[10]),
        float(info[11]),
        float(info[12]),
        float(info[13]),
        float(info[14]),
        float(info[15]),
        float(info[16]),
        float(info[17]),
        float(info[18]),
        float(info[19]),
        float(info[20]),
        float(info[21]),
        float(info[22]),
        float(info[23]),
        float(info[24]),
    ])
    # Utilizar el modelo
    prediction = Prediction(params, datosEntrada )
    return prediction
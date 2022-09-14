"""

"""
from Global.utils.db import get, post
from Global.utils.models import ADABOOST
import pandas as pd
import numpy as np


class Prediction:
    def __init__(self, json):
        """
        Metodo que crea una nueva prediccion con los datos enviados
        y guarda los resultados y la informacion en la base de datos.
        :param params:
        :return:
        """

        """
        SELECT id, name, email, phone, age, 
        country, form_data, transported
	    FROM public."User";
	    """

        import jsonpickle
        params = self.getParams(json)
        datosEntrada = self.getEntryData(json)
        self.id = None
        self.name = params[0]
        self.email = params[1]
        self.phone = params[2]
        self.age = params[3]
        self.country = params[4]
        self.transported = None
        self.transported = ADABOOST.predict(datosEntrada.reshape(1, -1))

        id = post("""INSERT INTO public."User"(name, email, phone, age, 
        country, form_data, transported) VALUES(%s, %s, %s, %s, %s, %s, %s) RETURNING id""", (self.name, self.email, self.phone, self.age,
                                                           self.country, jsonpickle.encode(datosEntrada), bool(self.transported)), returns=True)
        self.id = id


    def getParams(self, json):
        params = [
            json['name'],
            json['email'],
            json['phone'],
            json['age'],
            json['country'],
        ]
        return params

    def getEntryData(self, json):
        """
        Index(['cryo_sleep', 'age', 'vip', 'room_service', 'food_court',
           'shopping_mall', 'spa', 'vr_deck', 'transported', 'passenger_group',
           'Earth', 'Europa', 'Mars', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'P',
           'S', '55 Cancri e', 'PSO J318.5-22', 'TRAPPIST-1e'],
          dtype='object')"""
        datosEntrada = [
            float(json['cryo_sleep']),
            float(json['age']),
            float(json['vip']),
            float(json['room_service']),
            float(json['food_court']),
            float(json['shopping_mall']),
            float(json['spa']),
            float(json['vr_deck']),
            float(json['passenger_group']),
        ]
        if (json['home_planet']) == 'Earth':
            datosEntrada.extend([1, 0, 0])
        elif (json['home_planet']) == 'Europa':
            datosEntrada.extend([0, 1, 0])
        elif (json['home_planet']) == 'Mars':
            datosEntrada.extend([0, 0, 1])

        if(json['deck'] == 'A'):
            datosEntrada.extend([1, 0, 0, 0, 0, 0, 0])
        elif(json['deck'] == 'B'):
            datosEntrada.extend([0, 1, 0, 0, 0, 0, 0])
        elif (json['deck'] == 'C'):
            datosEntrada.extend([0, 0, 1, 0, 0, 0, 0])
        elif (json['deck'] == 'D'):
            datosEntrada.extend([0, 0, 0, 1, 0, 0, 0])
        elif (json['deck'] == 'E'):
            datosEntrada.extend([0, 0, 0, 0, 1, 0, 0])
        elif (json['deck'] == 'F'):
            datosEntrada.extend([0, 0, 0, 0, 0, 1, 0])
        elif (json['deck'] == 'G'):
            datosEntrada.extend([0, 0, 0, 0, 0, 0, 1])

        if json['side'] == 'T':
            datosEntrada.extend([1, 0, 0])
        elif json['side'] == 'P':
            datosEntrada.extend([0, 1, 0])
        elif json['side'] == 'S':
            datosEntrada.extend([0, 0, 1])

        if json['destiny'] == '55 Cancri e':
            datosEntrada.extend([1, 0, 0])
        elif json['destiny'] == 'PSO J318.5-22':
            datosEntrada.extend([0, 1, 0])
        elif json['destiny'] == 'TRAPPIST-1e':
            datosEntrada.extend([0, 0, 1])

        datosEntrada = np.array(datosEntrada)
        return datosEntrada

    def getReturn(self):
        return self.transported

class Model:
    def __init__(self):
        pass
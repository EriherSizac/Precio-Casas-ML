"""

"""
from Global.utils.db import get, post
from Global.utils.models import ADABOOST
import pandas as pd


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
        params = self.getParams()
        self.id = None
        self.name = params[0]
        self.email = params[1]
        self.phone = params[2]
        self.age = params[3]
        self.country = params[4]
        self.transported = None
        self.transported = ADABOOST.predict(datosEntrada.reshape(1, -1))
        print(self.transported)

        id = post("""INSERT INTO User(name, email, phone, age, 
        country, form_data, transported) RETURNING id""", (self.name, self.email, self.phone, self.age,
                                                           self.country, datosEntrada, self.transported))
        return self.transported

    def getParams(self, json):
        params = [
            json['name'],
            json['email'],
            json['phone'],
            json['age'],
            json['country'],
        ]
        return params

    def genEntryData(self, json):

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
        return datosEntrada

    def getReturn(self):
        return self.transported

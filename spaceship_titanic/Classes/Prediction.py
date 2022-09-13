"""

"""
from Global.utils.db import get, post
from Global.utils.models import ADABOOST
import pandas as pd


class Prediction:
    def __init__(self, params: [], datosEntrada):
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

    def getReturn(self):
        return self.transported

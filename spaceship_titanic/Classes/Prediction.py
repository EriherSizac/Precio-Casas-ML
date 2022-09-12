"""

"""
from Global.utils.db import get, post
from Global.utils.models import MODELO_EJERCICIOS
import pandas as pd
class Prediction:
    def ___init__(self, params: []):
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
        self.form_data = params[5]
        self.transported = None
        datosEntrada = self.getEntryDF(self.form_data)
        self.transported = MODELO_EJERCICIOS.predict(datosEntrada.reshape(1, -1))

        id = post("""INSERT INTO User(name, email, phone, age, 
        country, form_data, transported) RETURNING id""", (self.name, self.email, self.phone, self.age,
                                                           self.country, self.form_data, self.transported))
        return self.getReturn()

    def getReturn(self):
        return self.transported

    def getEntryDF(self, form_data):
        return None
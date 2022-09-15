"""

"""
from Global.utils.db import get, post, drop
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
        datosEntrada, datosJson = self.getEntryData(json)
        self.id = None
        self.name = params[0]
        self.email = params[1]
        self.phone = params[2]
        self.age = params[3]
        self.country = params[4]
        self.transported = None
        self.transported = ADABOOST.predict(datosEntrada.reshape(1, -1))

        id = post("""INSERT INTO public."User"(name, email, phone, age, 
        country, form_data, destination, transported) VALUES(%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id""", (self.name, self.email, self.phone, self.age,
                                                           self.country, jsonpickle.encode(json), json["destiny"] , bool(self.transported)), returns=True)
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

        return np.array(datosEntrada), datosEntrada

    def getReturn(self):
        return self.transported

class Model:
    @classmethod
    def getInfo(cls):
        survived = get("""select count(transported) as "Vivos", age
                        from public."User"
                        where transported = True
                        group by age order by age""",())
        total = get("""select count(transported) as "Vivos", age
                                from public."User"
                                group by age order by age""", ())

        percentagePerAge = get(
            """
            select count(age) as "TotalporEdad", age
            into table temp2
            from public."User"
            group by age;
            
            select count(transported) as "Vivos", age
            into table temp1
            from public."User"
            where transported = True
            group by age;
            
            select temp1."age", temp1."Vivos"::numeric/b."TotalporEdad"::numeric as "DATA"
            from temp1
            left join temp2 b on temp1."age" = b."age";
            """,()
        )
        drop("""drop table temp1, temp2;""")


        survivalPerc = pd.DataFrame(percentagePerAge)
        colsS = survivalPerc[0].to_list()
        colsP = [round(float(value), 2) for value in survivalPerc[1].to_list()]

        # Destinos

        percentagePerDest = get(
            """
            select count(destination) as "TotalporPlaneta", destination
            into table temp2
            from public."User"
            group by destination;
            
            select count(transported) as "Vivos", destination
            into table temp1
            from public."User"
            where transported = True
            group by destination;
            
            select temp1."destination", temp1."Vivos"::numeric/b."TotalporPlaneta"::numeric as "DATA"
            from temp1
            left join temp2 b on temp1."destination" = b."destination";
            """, ()
        )
        drop("""drop table temp1, temp2;""")

        survivalDest = pd.DataFrame(percentagePerDest)
        colsD = survivalDest[0].to_list()
        survivalDest = pd.DataFrame(survivalDest[1]).transpose()
        survivalDest.columns = colsD
        survivalDest = survivalDest.to_dict()
        try:
            survivalDest['55 Cancri e'][1] = round(float(survivalDest['55 Cancri e'][1]), 2)
        except:
            pass
        try:
            survivalDest['PSO J318.5-22'][1] = round(float(survivalDest['PSO J318.5-22'][1]), 2)
        except:
            pass
        try:
            survivalDest['TRAPPIST-1e'][1] = round(float(survivalDest['TRAPPIST-1e'][1]), 2)
        except:
            pass


        data = {
            "transported_vs_dead": {
                "transported": get("""SELECT COUNT(transported) FROM public."User" WHERE transported = True""",(),False)[0],
                "dead": get("""SELECT COUNT(transported) FROM public."User" WHERE transported = False""",(),False)[0]
            },
            "survival_ratio_age": {
                "age": colsS,
                "prob": colsP
            },
            "survival_ratio_destination": survivalDest
        }

        return data
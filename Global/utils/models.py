import os
from joblib import load
import os
# Cargar el modelo
MODELO_EJERCICIOS = load(os.environ.get('MODELS')+"/modeloArbol.joblib")
XGBOOST = load(os.environ.get('MODELS')+"/XGBoostFinal.joblib")
import numpy as np
from .model_01 import Model as Model01


class ForecastEnsemble(object):

    def __init__(self, cust_id):
        self.models = []
        import os
        print("path =", os.getcwd())
        self.models.append(Model01(path_to_csv="models/Dataset.csv", cust_id=cust_id))

    def predict(self, price):
        predictions = []
        for model in self.models:
            pred = model.predict(price)
            predictions.append(pred)
        return np.median(predictions)

import numpy as np
from .model_01 import Model as Model01


class ForecastEnsemble(object):
    """
    This is the class for ensemble prediction.

    Parameters
    ----------
    cust_id: int.
        Customer ID, an integer value between 0 and 99 (inclusive).

    """
    def __init__(self, cust_id):
        self.models = []
        import os
        self.models.append(Model01(path_to_csv="models/Dataset.csv", cust_id=cust_id))
        # If another model is also going to be used for model prediction, it should be appended to the list
        # (as above) here.

    def predict(self, price):
        """
        Predict order quantity based on drug price.

        Parameters
        ----------
        price: float.
            Price of the drug.

        Returns
        ----------
        median value of the ensemble predictions

        """
        predictions = []
        for model in self.models:
            pred = model.predict(price)
            predictions.append(pred)
        return np.median(predictions)

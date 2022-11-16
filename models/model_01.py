from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
import pandas as pd
import numpy as np


def build_and_train_generalized_linear_model(X_train, y_train, verbose=False):
    """
    Build and train a generalized linear model.

    Parameters
    ----------
    X_train: list of lists.
        Each list corresponds to a data point

    y_train: list.
        List of floats, each float corresponding to a data point.

    verbose: bool.
        Whether to spit out more information or not.

    Returns
    ----------
    pipe: sklearn machine-learning trained pipeline

    """
    if verbose:
        print(f"len(X_train) = {len(X_train)}")
        print(f"X_train = {X_train}")
        print(f"y_train = {y_train}")
    # construct the pipeline for model training
    pipe = Pipeline([('StandardScaler', StandardScaler()),
                     ('PolynomialFeatures', PolynomialFeatures()),
                     ('Ridge', Ridge(tol=0.00001)),
                     ])
    # Perform hyperparameter tuning on pipeline estimator with grid search
    param_grid = {"PolynomialFeatures__degree": np.arange(0, 5),
                  "Ridge__alpha": np.logspace(-4, 1, 10)  # 10^-4 to 10^1
                  }
    if len(X_train) > 4:
        pipe = GridSearchCV(estimator=pipe,
                            param_grid=param_grid,
                            cv=min(len(X_train) - 2, 4),
                            scoring="neg_mean_squared_error",
                            n_jobs=-1, verbose=0, return_train_score=True)
    else:
        pass  # If the number of data points is very small
        # (as is the case for CUST_ID = 48), we will ignore cross-validation

    pipe.fit(X_train.values, y_train)

    if verbose:
        print(f"train error: {pipe.score(X_train.values, y_train)}")
        print(f"best found parameters: {pipe.best_params_}")

    return pipe


class Model(object):
    """
    Machine learning model with fit and predict methods.

    Parameters
    ----------
    path_to_csv: str.
        Path to the csv file of training dataset

    cust_id: int.
        Customer ID.

    """
    def __init__(self, path_to_csv, cust_id):
        df = pd.read_csv(filepath_or_buffer=path_to_csv, parse_dates=['DATE'], low_memory=False)
        df = df[df.ORDER_QTY < 20000]
        cond = df.CUST_ID == cust_id
        X = df[cond][["PRICE_USD"]]
        y = df[cond]["ORDER_QTY"]
        self.pipe = self.fit(X, y)

    def fit(self, X, y):
        """
        Fit the model to the dataset.

        Parameters
        ----------
        X: list of lists.
            Each list corresponds to a data point

        y: list.
            List of floats, each float corresponding to a data point.

        Returns
        ----------
        pipe: sklearn machine-learning trained pipeline

        """
        self.pipe = build_and_train_generalized_linear_model(X, y, verbose=False)
        return self.pipe

    def predict(self, X):
        """
          Predict the model output for the input value.

          Parameters
          ----------
          X: list.
              List corresponding to a data point

          Returns
          ----------
          Float corresponding to a prediction.

          """
        return int(round(self.pipe.predict([[X]])[0]))

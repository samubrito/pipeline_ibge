from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import pandas as pd

class Modelo():
    def __init__(self):
        self.modelo = LinearRegression()

    def train(self, df:pd.DataFrame):
        X = df[["mes", "media_movel_3", "media_movel_6", "lag_1", "lag_3"]]
        y = df["taxa_de_desemprego"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, shuffle=False
        )

        self.modelo.fit(X_train, y_train)
        y_pred = self.modelo.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)


        return X_test.index, y_pred, mae
        
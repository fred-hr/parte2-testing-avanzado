from sklearn.linear_model import LinearRegression
import pandas as pd


class PredictiveModel:
    """
    Modelo predictivo basado en regresión lineal.
    Aprende de ejecuciones anteriores para predecir bugs futuros.
    """

    def __init__(self):
        self.model = LinearRegression()

    def train(self):
        data = pd.DataFrame({
            "execution": [1, 2, 3],
            "bugs_detected": [10, 20, 30],
        })

        x = data[["execution"]]
        y = data["bugs_detected"]

        self.model.fit(x, y)

        return data

    def predict(self, execution):
        future_execution = pd.DataFrame({
            "execution": [execution]
        })

        prediction = self.model.predict(future_execution)

        return round(float(prediction[0]), 2)

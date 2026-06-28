from sklearn.linear_model import LinearRegression
import pandas as pd


class CustomReliabilityModel:
    """
    Modelo predictivo personalizado de confiabilidad.
    Usa datos históricos, métricas de complejidad y patrones de uso.
    """

    def __init__(self):
        self.model = LinearRegression()

    def train(self):
        data = pd.DataFrame({
            "execution": [1, 2, 3, 4, 5],
            "test_cases": [100, 200, 300, 400, 500],
            "complexity": [3, 5, 6, 8, 9],
            "usage_frequency": [20, 35, 50, 65, 80],
            "previous_failures": [2, 4, 6, 9, 12],
            "reliability_score": [95, 90, 84, 76, 68],
        })

        x = data[[
            "execution",
            "test_cases",
            "complexity",
            "usage_frequency",
            "previous_failures"
        ]]

        y = data["reliability_score"]

        self.model.fit(x, y)

        return data

    def predict(self, execution, test_cases, complexity, usage_frequency, previous_failures):
        input_data = pd.DataFrame({
            "execution": [execution],
            "test_cases": [test_cases],
            "complexity": [complexity],
            "usage_frequency": [usage_frequency],
            "previous_failures": [previous_failures],
        })

        prediction = self.model.predict(input_data)

        return round(float(prediction[0]), 2)

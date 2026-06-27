import sys
from pathlib import Path
import json
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.predictive_model import PredictiveModel


def main():
    os.makedirs("reports", exist_ok=True)

    predictor = PredictiveModel()
    training_data = predictor.train()
    predicted_bugs = predictor.predict(4)

    report = {
        "training_data": training_data.to_dict(orient="records"),
        "prediction": {
            "next_execution": 4,
            "predicted_bugs": predicted_bugs,
        },
        "conclusion": (
            "El modelo predictivo estima la cantidad de bugs que podrían "
            "detectarse en una futura ejecución según datos históricos."
        ),
    }

    output_file = "reports/predictive_model_report.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("=" * 60)
    print("MODELO PREDICTIVO")
    print("=" * 60)
    print(training_data)
    print()
    print(f"Predicción ejecución 4 : {predicted_bugs} bugs")
    print(f"Reporte generado       : {output_file}")


if __name__ == "__main__":
    main()

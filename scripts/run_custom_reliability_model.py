import sys
from pathlib import Path
import json
import os

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.custom_reliability_model import CustomReliabilityModel


def main():
    os.makedirs("reports", exist_ok=True)

    model = CustomReliabilityModel()
    training_data = model.train()

    predicted_reliability = model.predict(
        execution=6,
        test_cases=600,
        complexity=10,
        usage_frequency=90,
        previous_failures=14
    )

    report = {
        "training_data": training_data.to_dict(orient="records"),
        "prediction_input": {
            "execution": 6,
            "test_cases": 600,
            "complexity": 10,
            "usage_frequency": 90,
            "previous_failures": 14
        },
        "predicted_reliability_score": predicted_reliability,
        "conclusion": (
            "El modelo estima la confiabilidad del sistema considerando "
            "datos históricos, complejidad del software, frecuencia de uso "
            "y fallos previos."
        )
    }

    output_file = "reports/custom_reliability_model_report.json"

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4, ensure_ascii=False)

    print("=" * 60)
    print("MODELO PREDICTIVO PERSONALIZADO DE CONFIABILIDAD")
    print("=" * 60)
    print(training_data)
    print()
    print(f"Predicción de confiabilidad ejecución 6: {predicted_reliability}%")
    print(f"Reporte generado: {output_file}")


if __name__ == "__main__":
    main()

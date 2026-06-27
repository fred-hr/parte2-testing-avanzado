import sys
from pathlib import Path
import json
import os
from collections import Counter

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.combinatorial_engine import generate_combinatorial_cases
from src.risk_prioritizer import prioritize_cases_by_risk


parameters = {
    "username": ["admin", "student", "guest", "unknown", ""],
    "password": ["Admin123", "Student123", "Guest123", "wrong", ""],
    "role": ["admin", "student", "guest", "invalid"],
    "device": ["known", "unknown"],
    "network": ["private", "public"],
    "two_factor_auth": ["enabled", "disabled"],
}


def build_risk_summary(prioritized_cases):
    summary = Counter(case["risk_level"] for case in prioritized_cases)

    return {
        "total_cases": len(prioritized_cases),
        "high": summary.get("high", 0),
        "medium": summary.get("medium", 0),
        "low": summary.get("low", 0),
        "highest_risk_case": prioritized_cases[0],
        "lowest_risk_case": prioritized_cases[-1],
    }


def main():
    os.makedirs("reports", exist_ok=True)

    cases = generate_combinatorial_cases(parameters)
    prioritized_cases = prioritize_cases_by_risk(cases)
    risk_summary = build_risk_summary(prioritized_cases)

    cases_file = "reports/combinatorial_cases.json"
    summary_file = "reports/risk_summary.json"

    with open(cases_file, "w", encoding="utf-8") as file:
        json.dump(prioritized_cases, file, indent=4, ensure_ascii=False)

    with open(summary_file, "w", encoding="utf-8") as file:
        json.dump(risk_summary, file, indent=4, ensure_ascii=False)

    print("=" * 60)
    print("ORQUESTACIÓN DE PRUEBAS COMBINATORIAS")
    print("=" * 60)
    print(f"Casos generados       : {len(prioritized_cases)}")
    print(f"Reporte de casos      : {cases_file}")
    print(f"Resumen de riesgos    : {summary_file}")
    print("=" * 60)

    print("\nRESUMEN DE RIESGO")
    print("-" * 60)
    print(f"Casos riesgo alto  : {risk_summary['high']}")
    print(f"Casos riesgo medio : {risk_summary['medium']}")
    print(f"Casos riesgo bajo  : {risk_summary['low']}")
    print(f"Total de casos     : {risk_summary['total_cases']}")

    print("\nTOP 5 CASOS DE MAYOR RIESGO")
    print("-" * 60)

    for case in prioritized_cases[:5]:
        print(case)

    print("\nCASO DE MENOR RIESGO")
    print("-" * 60)
    print(risk_summary["lowest_risk_case"])


if __name__ == "__main__":
    main()

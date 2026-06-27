def calculate_risk_score(test_case):
    """
    Calcula un puntaje de riesgo para cada caso de prueba.
    """

    score = 0

    if test_case.get("username") in ["", "unknown"]:
        score += 4

    if test_case.get("password") in ["", "wrong"]:
        score += 3

    if test_case.get("role") == "invalid":
        score += 2

    if test_case.get("device") == "unknown":
        score += 2

    if test_case.get("network") == "public":
        score += 2

    if test_case.get("two_factor_auth") == "disabled":
        score += 3

    return score


def classify_risk(score):
    """
    Clasifica el riesgo según el puntaje obtenido.
    """

    if score >= 9:
        return "high"

    if score >= 5:
        return "medium"

    return "low"


def prioritize_cases_by_risk(test_cases):
    """
    Agrega puntaje y nivel de riesgo a cada caso,
    luego los ordena de mayor a menor riesgo.
    """

    prioritized_cases = []

    for test_case in test_cases:
        score = calculate_risk_score(test_case)

        test_case["risk_score"] = score
        test_case["risk_level"] = classify_risk(score)

        prioritized_cases.append(test_case)

    prioritized_cases.sort(
        key=lambda case: case["risk_score"],
        reverse=True
    )

    return prioritized_cases

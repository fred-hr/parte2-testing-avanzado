from itertools import product


def generate_combinatorial_cases(parameters):
    """
    Genera automáticamente casos de prueba combinatorios
    a partir de un conjunto de parámetros.
    """

    keys = list(parameters.keys())
    values = list(parameters.values())

    combinations = product(*values)

    cases = []

    for index, combination in enumerate(combinations, start=1):
        case = dict(zip(keys, combination))
        case["case_id"] = index
        cases.append(case)

    return cases

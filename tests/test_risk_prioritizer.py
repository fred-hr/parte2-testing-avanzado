from src.risk_prioritizer import (
    calculate_risk_score,
    classify_risk,
    prioritize_cases_by_risk,
)


def test_calculate_high_risk_score():
    test_case = {
        "username": "unknown",
        "password": "wrong",
        "role": "invalid",
        "device": "unknown",
        "network": "public",
        "two_factor_auth": "disabled",
    }

    score = calculate_risk_score(test_case)
    assert score == 16


def test_classify_high_risk():
    assert classify_risk(10) == "high"


def test_classify_medium_risk():
    assert classify_risk(6) == "medium"


def test_classify_low_risk():
    assert classify_risk(2) == "low"


def test_prioritize_cases_by_risk():
    cases = [
        {
            "username": "admin",
            "password": "Admin123",
            "role": "admin",
            "device": "known",
            "network": "private",
            "two_factor_auth": "enabled",
        },
        {
            "username": "unknown",
            "password": "wrong",
            "role": "invalid",
            "device": "unknown",
            "network": "public",
            "two_factor_auth": "disabled",
        },
    ]

    prioritized = prioritize_cases_by_risk(cases)

    assert prioritized[0]["risk_level"] == "high"
    assert prioritized[0]["risk_score"] == 16
    assert prioritized[1]["risk_level"] == "low"

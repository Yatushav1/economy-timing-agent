def emotional_risk(data):
    risk = 0
    if data.decision_trigger == "fomo":
        risk += 2
    if data.stress_level == "high":
        risk += 2
    if data.confidence_level == "overconfident":
        risk += 1
    return risk

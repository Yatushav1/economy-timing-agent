def personal_risk(data):
    risk = 0
    if data.income_stability == "unstable":
        risk += 2
    if data.savings_buffer == "low":
        risk += 2
    if data.recent_regret == "yes":
        risk += 1
    return risk

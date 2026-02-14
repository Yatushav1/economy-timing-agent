def life_phase_risk(data):
    risk = 0
    if data.life_phase == "learning":
        risk += 1
    if data.goal_urgency == "low":
        risk += 1
    if data.flexibility == "high":
        risk -= 1
    return max(risk, 0)

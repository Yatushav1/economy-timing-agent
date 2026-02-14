from app.ai.explainer import generate_explanation

def evaluate_timing(data):

    score = 0

    if data.income == "low":
        score -= 1

    if data.income_stability == "unstable":
        score -= 2

    if data.savings_buffer == "low":
        score -= 2

    if data.stress_level == "high":
        score -= 1

    if data.goal_urgency == "high":
        score -= 1

    if data.decision_preference == "risky":
        score -= 1

    if score <= -4:
        decision = "WAIT"
        window = "Avoid taking action now"
    elif score <= -2:
        decision = "CAUTION"
        window = "Proceed carefully"
    else:
        decision = "SAFE"
        window = "Good time to act"

    reasons = f"""
Income: {data.income}
Income Stability: {data.income_stability}
Savings Buffer: {data.savings_buffer}
Stress Level: {data.stress_level}
Goal Urgency: {data.goal_urgency}
Decision Preference: {data.decision_preference}
"""

    explanation = generate_explanation(decision, reasons)

    return {
        "decision": decision,
        "opportunity_window": window,
        "explanation": explanation
    }

def explanation_prompt(decision, reasons):
    return f"""
Decision: {decision}

Reasons:
{reasons}

Explain this to the user in simple, calm language.
"""

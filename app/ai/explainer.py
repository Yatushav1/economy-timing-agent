import google.generativeai as genai
genai.configure(api_key="AIzaSyCjeZ-y6q-goiw4yLq5y_KAXdMwDiScFBA")
model = genai.GenerativeModel("models/gemini-flash-latest")

def generate_explanation(decision, reasons):

    prompt = f"""
You are an Economic Timing AI Agent.

Final Decision: {decision}

Risk Breakdown:
{reasons}

Explain clearly in simple human language why this decision was made.
Do not give financial advice.
Keep it under 20 words.
"""

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Explanation service temporarily unavailable."

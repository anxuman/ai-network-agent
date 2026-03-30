from openai import OpenAI
from config import client, MODEL

def analyze_output(results):

    prompt = f"""
You are a senior network engineer.

Analyze the outputs and give:
1. Root cause
2. Explanation
3. Fix

Be specific and technical.

Device Output:
{results}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Analyzer Error: {str(e)}"
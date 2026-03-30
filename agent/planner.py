from config import client, MODEL
import json
import re

def create_plan(user_input):

    prompt = f"""
You are an expert network engineer.

Create a troubleshooting plan based on the issue.

IMPORTANT:
- Use REALISTIC IPs, interfaces, and commands based on the problem
- Do NOT always use same commands
- Adapt to the issue

User Issue:
{user_input}

Return ONLY JSON:
[
  {{"step": 1, "action": "..."}}
]
"""

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )

        result = response.choices[0].message.content

        # 🔍 DEBUG (IMPORTANT)
        print("RAW LLM OUTPUT:\n", result)

        # 🧠 Extract JSON using regex
        json_match = re.search(r"\[.*\]", result, re.DOTALL)

        if not json_match:
            return "Planner Error: No JSON found in response"

        json_text = json_match.group(0)

        return json.loads(json_text)

    except Exception as e:
        return f"Planner Error: {str(e)}"
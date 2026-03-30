from openai import OpenAI
import json
import re
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL_NAME

# Initialize client
client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=NVIDIA_API_KEY
)

def extract_json(text):
    """Extract JSON from LLM response safely"""
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if match:
        return json.loads(match.group())
    return None


def create_plan(user_input):
    prompt = f"""
    Convert the user request into STRICT JSON.

    Example:
    Input: Check router R1
    Output:
    {{
      "device": "R1",
      "commands": ["show ip interface brief"]
    }}

    Rules:
    - Respond ONLY in JSON
    - No explanation
    - Always include device and commands

    User Input: {user_input}
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        response_text = completion.choices[0].message.content

        print("LLM RAW RESPONSE:", response_text)  # debug

        plan = extract_json(response_text)

        if not plan:
            return "Error: Could not parse JSON from LLM"

        return plan

    except Exception as e:
        return f"LLM Error: {str(e)}"
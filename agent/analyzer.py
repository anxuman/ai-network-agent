from openai import OpenAI
from config import NVIDIA_API_KEY, NVIDIA_BASE_URL, MODEL_NAME

# Initialize client
client = OpenAI(
    base_url=NVIDIA_BASE_URL,
    api_key=NVIDIA_API_KEY
)

def analyze_output(raw_output):
    prompt = f"""
    You are a network engineer.

    Analyze the following CLI output and explain:
    - What is the issue
    - Possible cause
    - Suggested fix

    Output:
    {raw_output}
    """

    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}"
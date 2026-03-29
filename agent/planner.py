import requests
from config import GLM_API_KEY

def create_plan(user_input):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": f"Bearer {GLM_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Convert the user request into JSON.

    Example:
    Input: Check router R1
    Output:
    {{
      "device": "R1",
      "commands": ["show ip interface brief"]
    }}

    User Input: {user_input}
    """

    data = {
        "model": "glm-5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    result = response.json()
    print(result) 
    return result["choices"][0]["message"]["content"]
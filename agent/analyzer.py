import requests
from config import GLM_API_KEY

def analyze_output(raw_output):
    url = "https://open.bigmodel.cn/api/paas/v4/chat/completions"

    headers = {
        "Authorization": f"Bearer {GLM_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Analyze the following network output and explain the issue:

    {raw_output}
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
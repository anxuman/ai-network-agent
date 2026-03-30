# config.py

from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

MODEL = "nvidia/nemotron-content-safety-reasoning-4b"


# 🔹 NETWORK DEVICES
DEVICES = {
    "R1": {
        "device_type": "cisco_ios",
        "host": "192.168.1.1",
        "username": "admin",
        "password": "admin"
    }
}
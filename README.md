# 🤖 AI Network Troubleshooting Agent

👨‍💻 Author
Anshuman Satpathy
Network Engineer | AI Enthusiast

An intelligent AI-powered network troubleshooting assistant that helps diagnose and analyze network issues using LLMs.

---

## 🚀 Features

- 🧠 AI-based troubleshooting planning
- ⚙️ Automated command execution (simulated)
- 📊 Intelligent analysis & root cause detection
- 💬 Interactive UI using Streamlit
- 🔄 Dynamic outputs (non-repetitive responses)

---

## 🏗️ Architecture
User Input
↓
Planner (LLM)
↓
Executor (Simulated Network Commands)
↓
Analyzer (LLM Diagnosis)
↓
Streamlit UI


---

## 📁 Project Structure
ai-network-agent/
│
├── app.py                  # Main entry point (CLI/UI)
├── config.py               # Device + API configs
│
├── agent/
│   ├── planner.py          # LLM → task planner
│   ├── executor.py         # Controls execution
│   ├── analyzer.py         # LLM → explanation
│
├── tools/
│   ├── network.py          # Netmiko functions
│
├── memory/
│   ├── context.json        # Store past queries (optional)
│
├── utils/
│   ├── helpers.py
│
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-network-agent.git
cd ai-network-agent
pip install -r requirements.txt

Edit config.py:

api_key = "YOUR_API_KEY"

#Run the App
python -m streamlit run app.py

⚠️ Disclaimer
This project uses simulated outputs for learning purposes.
Not intended for production use without real device integration.
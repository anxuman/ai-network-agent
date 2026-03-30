# app.py

import streamlit as st
from agent.planner import create_plan
from agent.executor import execute_plan
from agent.analyzer import analyze_output

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Network Agent",
    page_icon="🤖",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f4c75, #3282b8);
}

.main {
    background: transparent;
}

.center-box {
    text-align: center;
    margin-top: 100px;
}

.big-title {
    font-size: 32px;
    font-weight: 600;
    color: white;
}

.subtitle {
    font-size: 20px;
    color: #dbeafe;
    margin-bottom: 30px;
}

.stTextInput > div > div > input {
    border-radius: 20px;
    padding: 12px;
}

.suggestion-btn {
    margin: 5px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="center-box">
    <div class="big-title">Good Afternoon, Anshuman</div>
    <div class="subtitle">What can I help you with today?</div>
</div>
""", unsafe_allow_html=True)

# ---------------- INPUT BOX ----------------
user_input = st.text_input(
    " ",
    placeholder="Hello There how is your network today...",
    label_visibility="collapsed"
)

# ---------------- SUGGESTION BUTTONS ----------------
col1, col2, col3, col4, col5 = st.columns(5)

suggestions = [
    "Check router R1",
    "Why network slow?",
    "Check interface status",
    "Analyze logs",
    "Troubleshoot connectivity"
]

cols = [col1, col2, col3, col4, col5]

for i, suggestion in enumerate(suggestions):
    if cols[i].button(suggestion):
        user_input = suggestion

# ---------------- PROCESS INPUT ----------------
if user_input:

    st.divider()
    st.subheader("🔍 Processing Request...")

    # Step 1: Plan
    plan = create_plan(user_input)

    if isinstance(plan, str):
        st.error(plan)
    else:
        st.subheader("📋 Execution Plan")
        st.json(plan)

        # Step 2: Execute
        results = execute_plan(plan)

        st.subheader("🖥️ Device Output")
        for cmd, output in results.items():
            st.code(f"$ {cmd}\n{output}", language="bash")

        # Step 3: Analyze
        analysis = analyze_output(results)

        st.subheader("🧠 AI Diagnosis")
        st.success(analysis)
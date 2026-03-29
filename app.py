import json
from agent.planner import create_plan
from agent.executor import execute_plan
from agent.analyzer import analyze_output

def main():
    user_input = input("Hello Any Issue With the Network: ")

    plan = create_plan(user_input)
    plan = json.loads(plan)
    print("Plan:", plan)

    results = execute_plan(plan)
    print("Raw Output:", results)

    analysis = analyze_output(results)
    print("AI Analysis:", analysis)

if __name__ == "__main__":
    main()
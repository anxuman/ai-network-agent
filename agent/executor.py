from tools.network import run_command

def execute_plan(plan):
    device = plan.get("device")
    commands = plan.get("commands", [])

    results = {}

    for cmd in commands:
        results[cmd] = run_command(device, cmd)

    return results
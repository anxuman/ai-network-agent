import random

def execute_plan(plan):

    results = {}

    for step in plan:
        cmd = step.get("action", "")

        if "ping" in cmd:
            outcomes = [
                "Request timed out",
                "Reply from destination",
                "Destination unreachable"
            ]
            results[cmd] = random.choice(outcomes)

        elif "interface" in cmd:
            outcomes = [
                "Gig0/0 up\nGig0/1 up",
                "Gig0/0 down\nGig0/1 up",
                "Gig0/0 up\nGig0/1 down"
            ]
            results[cmd] = random.choice(outcomes)

        elif "traceroute" in cmd:
            results[cmd] = "Hop1 -> Hop2 -> Timeout -> Destination"

        else:
            results[cmd] = "Unknown command output"

    return results
import json
import random
import uuid
from datetime import datetime, timedelta

# Sample users and IPs
USERS = ["alice", "bob", "charlie", "diana", "admin"]
IPS = [
    "192.168.1.10",
    "192.168.1.20",
    "10.0.0.5",
    "172.16.0.8",
    "8.8.8.8"
]

def generate_login_event(is_attack=False):
    event = {
        "event_id": str(uuid.uuid4()),
        "event_time": datetime.utcnow().isoformat(),
        "username": random.choice(USERS),
        "source_ip": random.choice(IPS),
        "action": "LOGIN",
        "status": "SUCCESS"
    }

    if is_attack:
        event["status"] = "FAILED"

    return event

def generate_logs(file_name, total_events=100):
    logs = []

    for i in range(total_events):
        # Simulate brute-force attack every 20 events
        if i % 20 == 0:
            logs.append(generate_login_event(is_attack=True))
        else:
            logs.append(generate_login_event())

    with open(file_name, "w") as f:
        for log in logs:
            f.write(json.dumps(log) + "\n")

    print(f"Generated {total_events} security logs in {file_name}")

if __name__ == "__main__":
    generate_logs("security_logs.json", 100)

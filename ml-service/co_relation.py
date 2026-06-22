import time
import random

attack_graph = {
    "nodes": [],
    "edges": []
}

def generate_attack_event():
    ips = [
        "185.22.45.10",
        "103.89.12.8",
        "45.33.21.90",
        "192.168.1.10"
    ]

    countries = ["Russia", "China", "USA", "India", "Brazil"]
    attack_types = ["SQL Injection", "Botnet", "Phishing", "Ransomware"]

    return {
        "ip": random.choice(ips),
        "country": random.choice(countries),
        "attack": random.choice(attack_types),
        "timestamp": time.time()
    }


def update_graph(event):
    node = {
        "id": event["ip"],
        "label": event["country"],
        "group": event["attack"]
    }

    if node not in attack_graph["nodes"]:
        attack_graph["nodes"].append(node)

    # create correlation edges (same attack type = linked)
    for n in attack_graph["nodes"]:
        if n["group"] == node["group"] and n["id"] != node["id"]:
            edge = {
                "from": node["id"],
                "to": n["id"],
                "type": node["group"]
            }
            if edge not in attack_graph["edges"]:
                attack_graph["edges"].append(edge)

    return attack_graph
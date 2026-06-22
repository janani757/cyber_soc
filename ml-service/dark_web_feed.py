import random
import time

SOURCES = [
    "Ransomware forum leak",
    "Telegram hacker channel",
    "Pastebin dump",
    "TOR hidden service leak",
]

def generate_threat():
    return {
        "source": random.choice(SOURCES),
        "indicator": f"192.168.{random.randint(0,255)}.{random.randint(0,255)}",
        "type": random.choice(["Ransomware", "Phishing", "Botnet", "SQL Injection"]),
        "severity": random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"]),
        "timestamp": time.time()
    }
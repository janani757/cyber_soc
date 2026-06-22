import requests
import os

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")

def check_ip_reputation(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    res = requests.get(url, headers=headers, params=params)
    data = res.json()

    if "data" not in data:
        return {"risk": "unknown"}

    score = data["data"]["abuseConfidenceScore"]

    return {
        "ip": ip,
        "risk_score": score,
        "country": data["data"].get("countryCode"),
        "isp": data["data"].get("isp")
    }
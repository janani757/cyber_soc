def get_geo_risk(data):
    score = data.get("threat_score", 0)

    if score > 80:
        return {
            "country": "Russia",
            "risk": "HIGH"
        }
    elif score > 50:
        return {
            "country": "USA",
            "risk": "MEDIUM"
        }

    return {
        "country": "India",
        "risk": "LOW"
    }
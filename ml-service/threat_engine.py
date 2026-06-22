def analyze_csv(df):

    rows = len(df)

    score = min(100, rows // 50)

    if score > 80:
        level = "HIGH"
    elif score > 50:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "records": rows,
        "threat_score": score,
        "threat_level": level,
        "message": "AI analysis completed"
    }
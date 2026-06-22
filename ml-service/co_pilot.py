from memory_engine import remember, retrieve_memory

def analyze_incident(data, question=None):

    if question:
        past = retrieve_memory(question)

        if past:
            return {
                "answer": past,
                "source": "memory"
            }

    score = data.get("threat_score", 0)

    if score > 80:
        result = {
            "summary": "CRITICAL intrusion detected",
            "recommendation": "Block IP immediately"
        }
    elif score > 50:
        result = {
            "summary": "Suspicious activity detected",
            "recommendation": "Enable deep inspection"
        }
    else:
        result = {
            "summary": "Normal traffic",
            "recommendation": "No action required"
        }

    remember(str(data), result)
    return result
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def predict_malware(features):
    """
    features = [packet_size, duration, ports, flags]
    """
    arr = np.array(features).reshape(1, -1)
    pred = model.predict(arr)[0]

    return {
        "prediction": "MALICIOUS" if pred == 1 else "SAFE",
        "confidence": float(model.predict_proba(arr)[0][1]) if hasattr(model, "predict_proba") else None
    }
import numpy as np
import joblib
from tensorflow.keras.models import load_model

model = load_model("autoencoder.h5")
scaler = joblib.load("scaler.save")

THRESHOLD = 0.02  # anomaly cutoff

def detect_anomaly(features):
    """
    features = [packet_size, login_attempts, request_rate, geo_risk]
    """

    X = scaler.transform([features])
    recon = model.predict(X, verbose=0)

    error = np.mean(np.square(X - recon))

    return {
        "anomaly_score": float(error),
        "is_anomaly": error > THRESHOLD,
        "risk": "HIGH" if error > THRESHOLD else "LOW"
    }
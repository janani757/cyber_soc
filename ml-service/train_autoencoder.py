import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib
from tensorflow.keras import layers, models

# --------------------------
# SAMPLE NORMAL DATA (SOC FEATURES)
# [packet_size, login_attempts, request_rate, geo_risk]
# --------------------------
data = pd.DataFrame([
    [120, 2, 5, 0.1],
    [150, 1, 3, 0.2],
    [100, 2, 4, 0.0],
    [130, 1, 2, 0.1],
    [110, 3, 6, 0.2],
])

# --------------------------
# SCALE DATA
# --------------------------
scaler = MinMaxScaler()
X = scaler.fit_transform(data)

joblib.dump(scaler, "scaler.save")

# --------------------------
# AUTOENCODER MODEL
# --------------------------
model = models.Sequential([
    layers.Input(shape=(4,)),

    layers.Dense(8, activation="relu"),
    layers.Dense(3, activation="relu"),   # compressed representation

    layers.Dense(8, activation="relu"),
    layers.Dense(4, activation="sigmoid")
])

model.compile(optimizer="adam", loss="mse")

model.fit(X, X, epochs=50, verbose=1)

model.save("autoencoder.h5")

print("✅ Model trained and saved")
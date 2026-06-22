from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO
import random
import time

from co_pilot import analyze_incident
from anomaly_model import detect_anomaly

app = Flask(__name__)
CORS(app)

socketio = SocketIO(app, cors_allowed_origins="*")

# ----------------------------
# 🧠 COPILOT API
# ----------------------------
@app.route("/copilot", methods=["POST"])
def copilot():
    data = request.json
    result = analyze_incident(data)
    return jsonify(result)


# ----------------------------
# 🧬 ANOMALY DETECTION
# ----------------------------
@app.route("/anomaly-detect", methods=["POST"])
def anomaly_detect():
    data = request.json
    features = data.get("features", [])
    return jsonify(detect_anomaly(features))


# ----------------------------
# 🌍 GEO ATTACK DATA (MAP)
# ----------------------------
@app.route("/geo-attacks", methods=["GET"])
def geo_attacks():
    sample = [
        {"ip": "45.33.21.90", "lat": 37.77, "lon": -122.41, "score": 80},
        {"ip": "103.89.12.8", "lat": 28.61, "lon": 77.20, "score": 65},
        {"ip": "185.22.45.10", "lat": 55.75, "lon": 37.61, "score": 90},
    ]
    return jsonify(sample)


# ----------------------------
# 📊 DASHBOARD STATS
# ----------------------------
@app.route("/stats", methods=["GET"])
def stats():
    return jsonify({
        "labels": ["Mon", "Tue", "Wed", "Thu", "Fri"],
        "values": [10, 30, 20, 50, 40]
    })


# ----------------------------
# 🔴 LIVE ATTACK STREAM
# ----------------------------
def generate_event():
    return {
        "ip": f"192.168.1.{random.randint(1,255)}",
        "score": random.randint(10, 100),
        "status": random.choice(["SAFE", "SUSPICIOUS", "MALICIOUS"]),
        "message": "Real-time threat detected"
    }


def stream():
    while True:
        socketio.emit("threat_alert", generate_event())
        time.sleep(3)


@socketio.on("connect")
def handle_connect():
    socketio.start_background_task(stream)


# ----------------------------
# START SERVER
# ----------------------------
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=8000, debug=True)
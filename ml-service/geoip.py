import requests

def get_geo(ip):

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}")
        data = res.json()

        return {
            "country": data.get("country"),
            "lat": data.get("lat"),
            "lon": data.get("lon")
        }

    except:
        return {
            "country": "Unknown",
            "lat": 0,
            "lon": 0
        }
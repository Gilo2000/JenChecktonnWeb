import time
import requests

URL = "https://checkton.online"
API_KEY = "HoV4Ks77gmad7tEB89y3WADC3juoPcpNWX7pGL-DJCk""
DEVICE_ID = "and_2e381f5488921be0402be1f24b701cbd526133726237456d168b843a-89ba-442b-90e6-a0956a7c5873"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36",
    "X-Api-Key": API_KEY
}

payload = {
    "device_id": DEVICE_ID,
    "server": "global"
}

print("Starting cloud background request loop...", flush=True)

while True:
    try:
        response = requests.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code} | Response: {response.text}", flush=True)
        time.sleep(1.0)
    except requests.exceptions.RequestException as e:
        print(f"Network error encountered: {e}", flush=True)
        time.sleep(2.0)

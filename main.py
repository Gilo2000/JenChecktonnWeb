import os
import time
import cloudscraper

URL = "https://checkton.online"
API_KEY = "HoV4Ks77gmad7tEB89y3WADC3juoPcpNWX7pGL-DJCk"  # Keep your actual key here
DEVICE_ID = "and_2e381f5488921be0402be1f24b701cbd526133726237456d168b843a-89ba-442b-90e6-a0956a7c5873"  # Keep your actual ID here

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "X-Api-Key": API_KEY
}

payload = {
    "device_id": DEVICE_ID,
    "server": "global"
}

# Create the automated Cloudflare-bypass scraper instance
scraper = cloudscraper.create_scraper()

print("Starting request loop with Cloudflare bypass...", flush=True)

while True:
    try:
        response = scraper.post(URL, json=payload, headers=headers)
        print(f"Status Code: {response.status_code} | Response: {response.text}", flush=True)
        time.sleep(1.0)
    except Exception as e:
        print(f"Network error encountered: {e}", flush=True)
        time.sleep(2.0)

import csv
import requests

# --- LOGIN TO GET TOKEN ---
API_AUTH_URL = "http://127.0.0.1:8000/api/users/login/"
credentials = {
    "email": "mudakivictor@gmail.com",   # Or "username" depending on API
    "password": "7694mudvit"
}

response = requests.post(API_AUTH_URL, json=credentials)

if response.status_code == 200:
    tokens = response.json()
    ACCESS_TOKEN = tokens.get("access")
    REFRESH_TOKEN = tokens.get("refresh")

    if not ACCESS_TOKEN:
        print("❌ No access token received, check API response:", tokens)
        exit()

    print("✅ Login successful")
    print("Access Token:", ACCESS_TOKEN)
else:
    print(f"❌ Login failed: {response.status_code} - {response.text}")
    exit()

# --- CONFIGURATION ---
API_URL = "http://127.0.0.1:8000/products/brands/"
HEADERS = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
CSV_FILE = "electronics_brands.csv"

# --- POST DATA ---
with open(CSV_FILE, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        payload = {
            "name": row["brand"],
            "description": row["description"]
        }
        try:
            resp = requests.post(API_URL, json=payload, headers=HEADERS)
            if resp.status_code == 201:
                print(f"✅ Posted: {row['brand']}")
            else:
                print(f"⚠️ Failed for {row['brand']} - {resp.status_code} - {resp.text["name"]}")
        except requests.RequestException as e:
            print(f"❌ Error posting {row['brand']}: {e}")

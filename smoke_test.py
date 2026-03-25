import sys
import requests


response = requests.get("http://127.0.0.1:5000/health", timeout=5)


if response.status_code == 200 and response.json() == {"status": "ok"}:
    print("Smoke test passed.")
    
    
else:
    print("Smoke test failed.")
    sys.exit(1)

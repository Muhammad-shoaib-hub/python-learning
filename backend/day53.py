# day53.py
# Day 53: Virtual environments (venv) and pip

print("=== 📦 VIRTUAL ENVIRONMENTS & PIP DEMO ===\n")

# Importing a third-party package installed via pip
import requests

# Making a simple web request to a free test API
response = requests.get("https://api.github.com")

print(f"1. API Response Status Code: {response.status_code}")
if response.status_code == 200:
    print("✅ Successfully fetched data using the 'requests' library!")
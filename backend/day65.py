import requests

# 1. Define the API URL (endpoint)
url = "https://jsonplaceholder.typicode.com/todos/1"

# 2. Send a GET request to the URL
response = requests.get(url)

# 3. Check the HTTP status code (200 means Success)
print(f"Status Code: {response.status_code}")

# 4. Extract and print the JSON response data as a Python dictionary
data = response.json()
print("Response Data:", data)

# 5. Access specific fields like a normal Python dictionary
print(f"\nTask Title: {data['title']}")
print(f"Is Completed?: {data['completed']}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


import requests

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Status Code:", response.status_code)
    print("Title:", data["title"])
    print("Completed:", data["completed"])
else:
    print("Failed to fetch data:", response.status_code)
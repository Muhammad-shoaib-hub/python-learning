import requests

# 1. API endpoint for creating a new post
url = "https://jsonplaceholder.typicode.com/posts"

# 2. Data we want to send (Python Dictionary)
new_post = {
    "title" : "My Day 66 Practice",
    "body" : "Learning post request in python",
    "userId" : 1
}

# 3. Send the POST request using the json parameter
response = requests.post(url, json=new_post)

# 4. Check status code (201 means "Created")
print("Status Code : ", response.status_code)

# 5. Print the server's response
if response.status_code == 201:
    print("Successfully created post!")
    print("Response from server:", response.json())
else:
    print("Failed to create post.")

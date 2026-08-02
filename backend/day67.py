import requests

# 1. Fetch a list of multiple posts
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    posts = response.json()  # This returns a LIST of dictionaries
    
    print(f"Total posts received: {len(posts)}")
    print("-" * 40)
    
    # 2. Loop through the first 5 posts and extract specific JSON fields
    print("--- First 5 Posts ---")
    for post in posts[:5]:
        print(f"ID: {post['id']} | Title: {post['title']}")
        
    print("-" * 40)
    
    # 3. Filter JSON data: Find all posts written by userId == 2
    user2_posts = [p for p in posts if p["userId"] == 2]
    print(f"Total posts by User 2: {len(user2_posts)}")

else:
    print(f"Error fetching data: {response.status_code}")

# its only for to enjoy it 


# ==========================================
# DAY 74: DICTIONARY & SET COMPREHENSIONS
# ==========================================

# 1. Dictionary: Map student names to their passing status (>= 50)
scores = {"Shoaib": 85, "Ali": 42, "Ahmad": 78, "Sara": 35}
pass_status = {name: ("Pass" if score >= 50 else "Fail") for name, score in scores.items()}

print("--- 1. Student Pass/Fail Status ---")
print(pass_status)


# 2. Dictionary: Filter user data (Backend API use-case: active users only)
users = [
    {"username": "shoaib", "active": True},
    {"username": "guest1", "active": False},
    {"username": "ahmad", "active": True}
]
active_user_dict = {u["username"]: u["active"] for u in users if u["active"]}

print("\n--- 2. Active Users Dict ---")
print(active_user_dict)


# 3. Set: Extract unique categories from product data (removes duplicates)
products = [
    {"name": "Laptop", "category": "Electronics"},
    {"name": "Shirt", "category": "Apparel"},
    {"name": "Phone", "category": "Electronics"},
    {"name": "Jeans", "category": "Apparel"},
]
unique_categories = {p["category"] for p in products}

print("\n--- 3. Unique Categories Set ---")
print(unique_categories)


# 4. Set: Extract unique tags from a list with spaces/mixed casing
raw_tags = [" python ", "PYTHON", " Django", "django ", "API"]
clean_tags = {tag.strip().upper() for tag in raw_tags}

print("\n--- 4. Clean Unique Tags Set ---")
print(clean_tags)
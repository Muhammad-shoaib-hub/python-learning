# day25.py

print("--- 1. Testing Local vs Global Variables ---")

# Global variable (created outside, visible everywhere)
user_role = "Admin"
def check_access():
    # Local variable (created inside, visible ONLY inside this function)
    secret_code = 1234

    print(f"inside function -> Role = {user_role}")
    print(f"inside function -> secret code = {secret_code}")

check_access()

print(f"outside function -> Role = {user_role}")


print("\n")
print("\n")
print("\n")

print("\n--- 2. Modifying a Global Variable (`global` keyword) ---")

secor = 0
def add_points():
    global secor # Tells Python: "We want to change the score outside!"
    secor = secor + 4
    print(f"inside the function -> score update to = {secor}")

print(f"score before the function = {secor}")
add_points()
print(f"score after the function = {secor}")


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("Create a Global Variable:")
player_coins = 100

print("Part 1: Local Scope Function (show_inventory)")
def show_university():
    invertory_item = "shiled"
    print(f"player coins = {player_coins} : invertory item = {invertory_item}")

show_university()

print("\n")
print("\n")

print("Part 2: Modifying Global Scope (buy_item)")
def buy_item(item_cost):
    global player_coins
    remaining_balance = player_coins - item_cost
    print(f"the remaining coins are = {remaining_balance}")

buy_item(40)
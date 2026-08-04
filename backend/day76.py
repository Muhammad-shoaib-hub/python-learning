# ==========================================
# 1. THE DECORATOR (The Outfit / Wrapper)
# ==========================================

def party_outfit(original_founction):

    # This inner function 'wrapper' is the actual box!
    def wrapper():
        print("[BEFORE] Putting on a fancy party hat...")

        # Now run the actual function you handed in!
        original_founction()

        print("[AFTER] Blowing the party horn! Party is over!")

    return wrapper      # # Hand back the wrapped package!

# ==========================================
# 2. YOUR ORIGINAL FUNCTION
# ==========================================

@party_outfit    #  <--- This puts the party outfit on make_pizza!

def make_piza():
    print("🍕 Making a delicious pepperoni pizza!")

# ==========================================
# 3. CALLING THE FUNCTION
# ==========================================
make_piza()




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# 🎯 Challenge: The Security Guard Decorator

print("--- 🎯 Challenge: The Security Guard Decorator---")

def security_guard(func):

    def checking_security():
        print("🔒 [BEFORE] Security check: Verifying user ID...")

        func()

        print("🔓 [AFTER] Security check complete: Access granted!")

    # must remember this part please
    return checking_security

@security_guard 
def open_secret_vault():
    print("💰 Vault Opened: Welcome to the secret chamber!")

# 3. CALLING THE FUNCTION
open_secret_vault()
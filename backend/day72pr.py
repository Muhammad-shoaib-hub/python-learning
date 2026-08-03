import re

# ==========================================
# PART 1: VALIDATION FUNCTIONS
# ==========================================

def validate_email(email):
    # ^ = start of string, $ = end of string
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" 
    if re.match(pattern, email):
        return True
    return False

def validate_password(password):
    """
    Password Rules:
    - At least 8 characters
    - At least 1 digit 
    - At least 1 uppercase letter ([A-Z])
    """

    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    return True


# ==========================================
# PART 2: EXTRACTION FROM LOG TEXT
# ==========================================

log_data = """
[2026-08-01 10:15:30] USER_LOGIN user_id=101 status=SUCCESS
[2026-08-02 14:22:05] ERROR failed connection to server_id=502
[2026-08-03 09:00:12] USER_LOGOUT user_id=101 status=SUCCESS
"""

def extract_date(text):
    # Extracts all YYYY-MM-DD dates
    date_pattern = r"\b\d{4}-\d{2}-\d{2}\b"


    # must remember this part
    return re.search(date_pattern, text)


# ==========================================
# RUNNING THE DEMO
# ==========================================

if __name__ == "__main__":
    print("--- 🔍 REGEX VALIDATION DEMO ---")

    test_email = ["shoaib@gmail.com", "invalid-email@", "user.name@domain.co"]
    for email in test_email:
        is_valid = validate_email(email)
        if is_valid == True:
            status = "valid"
        else:
            status = "non-valid"
        print(f"Email : {email:<25} - Status : {status}")  # must remember this line please



    print("\n--- 🔐 PASSWORD VALIDATION DEMO ---")

    test_password = ["short", "nodigitshere", "Password123", "lower1234"]
    for pwd in test_password:
        is_valid = validate_password(pwd)
        if is_valid == True:
            status = "valid"
        else:
            status = "non-valid"
        print(f"Password is : {pwd:<20} - Status is : {status}")



    print("\n--- 📅 DATA EXTRACTION DEMO ---")

    found_dates = extract_date(log_data)
    print(f"Extracted Log Dates : {found_dates}")
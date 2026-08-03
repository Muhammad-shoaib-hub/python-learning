# 🔍 Core re Module Functions

# 1. re.search(pattern, text)
# Scans through a string and returns a Match object for the first match found (or None if no match exists).


import re

text = "My order ID is 45930"
match = re.search(r"\d+", text)

if match:
    print("Found match : ", match.group())

print("\n")


# 2. re.findall(pattern, text)
# Returns a list of strings containing all non-overlapping matches in the string.

import re

text = "Items cost $45, $120, and $5."
price = re.findall(r"\d+", text)

print(price)


print("\n")

# 3. re.sub(pattern, replacement, text)
# Replaces all occurrences of the pattern with a replacement string.

import re

text = "Call me it 38289392 or 383928223"
call_number = re.sub(r"\d", "*", text)

print(call_number)




print("\n")


# its just for fun

import re

text = "Call me it 38289392 or 383928223"
call_number = re.sub(r"\b", "*", text)

print(call_number)




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



import re

text = "Contact support@example.com or admin@domain.org for help."

# 1. Find all digits in this sentence
numbers_text = "There are 12 apples, 5 bananas, and 100 oranges."
digits = re.findall(r"\d+", numbers_text)
print("Extracted Numbers:", digits)

# 2. Extract email addresses using regex
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print("Extracted Emails:", emails)

# 3. Mask digits in text
sensitive_data = "Account code is 9876"
masked_data = re.sub(r"\d", "#", sensitive_data)
print("Masked Data:", masked_data)




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



import re

raw_text = "Users user_101 and user_405 logged in. Secret code: 9988."
raw_text1 = re.findall(r"\d+", raw_text)
print("Extracted Numbers:", raw_text1)


print("\n")

raw_text = "Users user_101 and user_405 logged in. Secret code: 9988."
raw_text2 = re.sub(r"\d", "*", raw_text)
print("Masked Text:", raw_text2)
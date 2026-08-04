import re  

def execution_tracker(func): 
    def wrapper(text):  
        print("[LOG] Processing started...")  # 
        result = func(text)  
        print("[LOG] Processing completed!") 
        return result  # sends the original function's result back out, so nothing is lost
    return wrapper 

@execution_tracker  
def extract_product_codes(text):  # this function finds all product codes inside some text
    codes = re.findall(r"PROD-\d{4}", text)  # find every match of "PROD-" followed by exactly 4 digits
    return codes  # send the list of matches back to whoever called this function


@execution_tracker 
def extract_prices(text):  # this function finds all prices inside some text
    prices = re.findall(r"\$[0-9]+\.[0-9]{2}", text)  
    return prices 

@execution_tracker 
def extract_emails(text): 
    emails = re.findall(r"\w+@(support\.com|help\.org)", text)  # match word characters + @ + either allowed domain
    return emails  


def stream_clean_data(items):  # a generator function — takes a list and hands out items one at a time
    for item in items:  # go through each item in the list, one by one
        yield "• " + item  # pause here and hand back this one item, formatted with a bullet in front


raw_support_text = """
Ticket #104: Customer bought PROD-1024 for $49.99. Issue reported to help@support.com.
Ticket #105: Returned item PROD-9021 priced at $120.50. Contact agent at care@help.org.
Invalid code PROD-12 and bad price $10. Contact personal email test@gmail.com instead.
Ticket #106: Purchased PROD-4455 for $299.00. Escalated to manager@support.com.
"""  # this is the raw block of text we'll be scanning for matches

codes = extract_product_codes(raw_support_text)  # run the decorated function, printing logs + getting the code matches
print("Product Codes:")  # print a header before the results
for line in stream_clean_data(codes):  # loop through the generator, pulling one bulleted item at a time
    print(line)  # print each bulleted product code

prices = extract_prices(raw_support_text)  # run the decorated function, printing logs + getting the price matches
print("\nPrices:")  # print a header (with a blank line before it) before the results
for line in stream_clean_data(prices):  # loop through the generator again, this time with prices
    print(line)  # print each bulleted price




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



# this is without comments please here


import re


def execution_tracker(func):
    def wrapper(text):
        print("[LOG] Processing started...")
        result = func(text)
        print("[LOG] Processing completed!")
        return result
    return wrapper


@execution_tracker
def extract_product_codes(text):
    codes = re.findall(r"PROD-\d{4}", text)
    return codes


@execution_tracker
def extract_prices(text):
    prices = re.findall(r"\$[0-9]+\.[0-9]{2}", text)
    return prices


@execution_tracker
def extract_emails(text):
    emails = re.findall(r"\w+@(support\.com|help\.org)", text)
    return emails


def stream_clean_data(items):
    for item in items:
        yield "• " + item


raw_support_text = """
Ticket #104: Customer bought PROD-1024 for $49.99. Issue reported to help@support.com.
Ticket #105: Returned item PROD-9021 priced at $120.50. Contact agent at care@help.org.
Invalid code PROD-12 and bad price $10. Contact personal email test@gmail.com instead.
Ticket #106: Purchased PROD-4455 for $299.00. Escalated to manager@support.com.
"""

codes = extract_product_codes(raw_support_text)
print("Product Codes:")
for line in stream_clean_data(codes):
    print(line)

prices = extract_prices(raw_support_text)
print("\nPrices:")
for line in stream_clean_data(prices):
    print(line)
import requests

def convert_currency(base_currency, target_currency, amount):
    base_currency = base_currency.upper().strip()
    target_currency = target_currency.upper().strip()
    
    url = f"https://open.er-api.com/v6/latest/{base_currency}"
    
    print(f"\n🔍 Fetching live rates for {base_currency}...")
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and data.get("result") == "success":
            rates = data.get("rates", {})
            
            if target_currency in rates:
                rate = rates[target_currency]
                converted_amount = amount * rate
                
                print("=" * 40)
                print(f"💵 Base Amount: {amount:.2f} {base_currency}")
                print(f"💱 Exchange Rate: 1 {base_currency} = {rate:.4f} {target_currency}")
                print(f"🎉 Converted Total: {converted_amount:.2f} {target_currency}")
                print("=" * 40)
            else:
                print(f"❌ Target currency '{target_currency}' not found.")
        else:
            print(f"❌ Error fetching data. Status: {response.status_code}")
            
    except Exception as error:
        print(f"⚠️ An error occurred: {error}")

if __name__ == "__main__":
    print("--- 💱 LIVE CURRENCY CONVERTER 💱 ---")
    
    base = input("Enter base currency (e.g., USD, EUR, GBP): ") or "USD"
    target = input("Enter target currency (e.g., PKR, EUR, INR): ") or "PKR"
    
    try:
        amount_input = float(input("Enter amount to convert: ") or 100)
        convert_currency(base, target, amount_input)
    except ValueError:
        print("❌ Invalid amount entered. Please enter a number.")
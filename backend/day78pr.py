import argparse

shoping = argparse.ArgumentParser(description="trying to buy somthing")

shoping.add_argument("--price", type=float, default=100, help="its a the price of it")
shoping.add_argument("--discount", type=float, default=20, help="here we have the discount with 20")

sho = shoping.parse_args()

Final_price = sho.price - (sho.price * sho.discount/100)

print(f"🏷️ Original Price: {sho.price}")
print(f"✂️ Discount: {sho.discount}")
print(f"🎉 Final Price: {Final_price}")
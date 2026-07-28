# day29.py
# handle built-in Python errors
# handle built-in Python errors 

print("--- 1. Basic Try / Except ---")

try:
    number = int(input("please enter nunmber to divid 100 by = "))
    result = 100/number
    print(f"100 / {number} = {result}")

except ZeroDivisionError:
    print("error :you cannot divid by 0 ")
except ValueError:
    print("error : this was not a vaild number")

print("\n")
print("\n")

print("\n--- 2. Try / Except / Else / Finally ---")

try:
     print("Attemptting to convert input")
     num1 = int(input("please enter your age = "))

except ValueError:
    print("Error : please enter you age in numbers like 23, 53, etc ")
else:
    print(f" good : your age added to {num1}")
finally:
    print("system check complete ")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

def convert_text_int(text):
    try:
        converted = int(text)
        print("the convert text is here = ", converted)
        return converted
    except ValueError:
        print("Error: Invalid input: Not a number!")

# Now test both calls:
convert_text_int("42")
convert_text_int("hello")


print("\n")
print("\n")


def safe_divide(a,b):
    try:
        calculate = a/b
        print("the divide value is here = ", calculate)
        return calculate

    except ZeroDivisionError:
        print("error : can not divide by 0 ")
    else:
        print(f"Calculation successful! Result {calculate}")
    finally:
        print("Division attempt finished.")

safe_divide(10, 3 ) 
safe_divide(30, 0)
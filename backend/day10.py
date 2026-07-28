guess = ""
while guess != "python":
    guess = input("guess the secret language name = ")
    if guess != "python":
        print("wrong guess ! try again")
print("you found the secret language name = ", guess)



num1 = int(input("please enter a number ( 5 or 10) = "))
while num1 > 0:
    print("your current number is = ", num1)
    num1 = num1 -1
print("the program is finished")



guess1 = input("please enter the secret language name please = ")
while guess1 != "python1":
    print("wrong guess, try again")
    guess1 = input("please enter the secret language name please = ")
print("correct! you found it ")



savings = 0
while savings < 50:
    savings1 = int(input("how much money do you have? = "))
    savings = savings + savings1
    print("you current total saving is = ", savings)
    print("-" * 30)
print(f"congratulations! your goal reached total save: is {savings}")
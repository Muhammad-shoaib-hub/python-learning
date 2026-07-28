import random

# a computer pick a secret number between 1 to 20
s_number = random.randint(1,20)

print("welcome to the number gussing game")
print("i am thinking a numbe between 1 to 20")
print("-"*70)

# start a while loop from here 
while True:
    guess = int(input("please enter a number for guessing = "))

    if guess < s_number:
        print("too loo try another number")
    elif guess > s_number:
        print("too high try another number please")
    else:
        print("you guess the secret number = ",guess)
        break
print("thank you for playing with me")



print("-"*70)
print("-"*70)
print("-"*70)
print("-"*70)
print("-"*70)



num1 = 45

while True:
    guess1 = int(input("please enter your number to guess it = "))

    if guess1 > num1:
        print("too higher try another number")
    elif guess1 < num1:
        print("too low try another number")
    else:
        print("you found the secret number = ", guess1)
        break
print("you are playing very well")

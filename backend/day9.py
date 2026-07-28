age = int(input("please enter you age = "))
has_license = True
if age >= 18:
    print("you are old enough to dirve ")
    if has_license:
        print("you are allowed to drive ")
    else:
        print("you are not allowed to drive ")
else:
    print("you are too younge ") 




age = int(input("please enter you age = "))
has_license = input("Do you have a driving  license? (yes/no) ")
if age >= 18:
    print("you are old enough to dirve ")
    if has_license == "yes":
        print("you are allowed to drive ")
    else:
        print("you are not allowed to drive ")
else:
    print("you are too younge ") 




username = input("please enter your name plese = ")
passwoard = input("please enter your passwoard")
if username == "admin":
    if passwoard == "123456":
        print("Access Granted")
    else:
        print("wrong password")
else:
    print("wrong user name")
 
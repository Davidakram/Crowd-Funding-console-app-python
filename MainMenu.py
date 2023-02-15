
import os
os.system("clear")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MainMenu~~~~~~~~~~~~~~~~~~~~")
print("Do you want to sign in or register?")
reply = input()
while reply != "signin" and reply != "register":
    print("Please enter either 'signin' or 'register'")
    reply = input()
else:
    if reply == "signin":
        os.system("clear")
        os.system("python3 Login.py")
    else:
        os.system("clear")
        os.system("python3 registertion.py")

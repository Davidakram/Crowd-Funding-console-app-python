import re
import time
import os
check = open("Users.txt", "r")
users = check.readlines()


def validatingUserName():
    os.system("clear")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Registration~~~~~~~~~~~~~~~~~~~~~")
    print("Please enter your first name")
    name = input()
    while not name.isalpha():
        print("Please enter a valid name")
        name = input()
    else:

        for x in range(len(users)):
            while users[x].split(":")[1] == name:
                print(f"{name} is already taken  ")
                print("enter a new name")
                name = input()
    return name


userName = validatingUserName()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validatingLastName():
    print("Please enter your last name")
    lastName = input()
    while not lastName.isalpha():
        print("Please enter a valid last name")
        lastName = input()
    else:
        for x in range(len(users)):
            while users[x].split(":")[2] == lastName:
                print(f"{lastName} is already taken  ")
                print("enter a new last name")
                lastName = input()

    return lastName


Lastname = validatingLastName()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validatingEmail():
    emailvalidform = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    print("Please enter your email")
    email = input()
    while not re.fullmatch(emailvalidform, email):
        print("Please enter a valid email")
        email = input()
    else:

        for x in range(len(users)):

            while users[x].split(":")[3] == email:
                print(f"{email} is already registered ")
                print("enter a new email")
                email = input()

    return email


userEmail = validatingEmail()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validatingPassword():
    print("Please enter your password")
    password = input()
    while len(password) < 8:
        print("Password must be at least 8 characters long")
        password = input()
    else:
        return password


userPassword = validatingPassword()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validatingRepeatedPassword():
    print("please enter your password again")
    repeatedPassword = input()
    while repeatedPassword != userPassword:
        print("passwords do not match & try again ")
        repeatedPassword = input()
    else:
        return repeatedPassword


userRepetetedPassword = validatingRepeatedPassword()
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def validatingPhoneNumber():
    print("Please enter your phone number after +2")
    phoneNumber = input()
    while not phoneNumber.isnumeric():
        print("Phone Number must contain only numbers")
        phoneNumber = input()
    else:
        while len(phoneNumber) != 11:
            print("Phone Number must be 11 digits long")
            phoneNumber = input()
        else:
            while phoneNumber[0:3] != '010' and phoneNumber[0:3] != '012' and phoneNumber[0:3] != '011' and phoneNumber[0:3] != '015':
                print("Phone Number must starts with 010,012,011,015,")
                phoneNumber = input()
            else:

                for x in range(len(users)):
                    while phoneNumber in users[x].split(":")[5][2:]:
                        print(f"{phoneNumber} is already taken  ")
                        print("enter a new phone number")
                        phoneNumber = input()

            return f"+2{phoneNumber}"


mobileNumber = validatingPhoneNumber()
id = round(time.time())
usersFile = open("Users.txt", "a")
usersFile.write(
    f"{id}:{userName}:{Lastname}:{userEmail}:{userPassword}:{mobileNumber}\n")
usersFile.close()
os.system("python3 Login.py")

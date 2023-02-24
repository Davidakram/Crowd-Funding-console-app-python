import re
import os
import psycopg2

dbuser = "postgres"
dbPassword = "david"
dbname = "pythontask"


def validatingUserName():
    os.system("clear")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~Registration~~~~~~~~~~~~~~~~~~~~~")
    print("Please enter your first name")
    name = input()
    while not name.isalpha():
        print("Please enter a valid name")
        name = input()
    else:
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
        connection = psycopg2.connect(
            user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
        dbcursor = connection.cursor()
        query_select = "select useremail from usersdata "
        dbcursor.execute(query_select)
        connection.commit()

        rec = dbcursor.fetchall()
        for rec in rec:
            while rec[0] == email:
                print("Email already exists")
                print("Please enter a different email")
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

                return phoneNumber


mobileNumber = validatingPhoneNumber()

try:
    connection = psycopg2.connect(
        user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
    dbcursor = connection.cursor()
    query_insert = f"insert into usersdata(username,lastname,useremail,userpassword,usermobile) values('{userName}','{Lastname}','{userEmail}','{userPassword}',{mobileNumber}) "
    dbcursor.execute(query_insert)
    connection.commit()
    dbcursor.close()
    connection.close()
    os.system("python3 Login.py")
except Exception as error:
    print(error)

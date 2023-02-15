import os
import re
from subprocess import check_output

user = ''


def create_project():
    print("please enter the project name")
    projectName = input()
    if f"{projectName}.txt" in os.listdir("/media/lenovo/E/ITI content/python/day3/{user}Projects".format(user=user)):
        print("Project already exists")
        create_project()
    else:
        os.system(
            f"cd {user}Projects && touch {projectName}.txt")
        print(f"Project {projectName} was created successfully")
        print("enter some details about the project")
        details = input()
        while details == "":
            print("please enter details")
            details = input()
        else:
            print("please enter your predicted target")
            target = input()
            while not target.isnumeric():
                print("please enter a number")
                target = input()
            else:
                projectFile = open(f"{user}Projects/{projectName}.txt", "w")
                projectFile.write(
                    f"--------------------{projectName}--------------------\n details:{details}\n target:{target}\n")
                projectFile.close()
                print(
                    f"Project named {projectName} was created successfully :)")
                exit()


def create_project_Directory():
    if f"{user}Projects" not in os.listdir():
        os.system("mkdir {user}Projects".format(user=user))
        print(f"{user}Project Directory Created")
        create_project()

    else:
        print("Project Directory already exists")
        print("do you want to create a new project inside your directory?")
        answer = input()
        while answer != "yes" and answer != "no":
            print("please enter yes or no")
            answer = input()
        else:
            if answer == "yes":
                create_project()
            else:
                exit()

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


def logining_in():
    os.system("clear")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~Logining in~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("please enter your email ")
    emailvalidform = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"

    email = input()
    while not re.fullmatch(emailvalidform, email):
        print("Please enter a valid email")
        email = input()
    else:
        usersFile = open("Users.txt", "r")
        users = usersFile.readlines()
        for x in range(len(users)):
            if users[x].split(":")[3] == email:
                userPassword = users[x].split(":")[4]
                userName = users[x].split(":")[1]
                global user
                user = userName
                print("please enter your passsword")
                enterpassword = input()
                while not re.fullmatch(userPassword, enterpassword):
                    print(" InCorrect Passsword & Please enter the correct password")
                    enterpassword = input()
                else:
                    os.system("clear")
                    print(
                        f"-------------------Welcome {userName}--------------------")

                    print("Have you done any projects before ?")
                    answer = input()
                    while answer != "yes" and answer != "no":
                        print("please enter yes or no")
                        answer = input()
                    else:
                        if answer == "yes":

                            if f"{user}Projects" not in os.listdir():
                                print("there is no project directory for you ")
                                print("do you want to create a new Directory")
                                rep = input()
                                while rep != "yes" and rep != "no":
                                    print("enter yes or no")
                                    rep = input()
                                else:
                                    if rep.lower() == "yes":
                                        create_project_Directory()
                                    else:
                                        print("goodbye  :) ")
                                        exit()
                            else:

                                print(
                                    "do you want to list your projects or create a new project ?")
                                reply = input()
                                while reply != "create" and reply != "list":
                                    print("enter list or create")
                                    reply = input()
                                else:
                                    if reply.lower() == "create":
                                        create_project()
                                    else:
                                        print("here are your previous projects")

                                        os.system(f"cd {user}Projects && ls ")
                                        print(
                                            "do you want to delete a project or edit a project?")
                                        gawab = input()
                                        while gawab != 'delete' and gawab != 'edit':
                                            print("enter delete or edit")
                                            gawab = input()
                                        else:
                                            if gawab == "delete":
                                                print(
                                                    "enter the name of the prjoect you want to delete")
                                                deleteproject = input()

                                                while not f"{deleteproject}.txt" in os.listdir("/media/lenovo/E/ITI content/python/day3/{user}Projects".format(user=user)):
                                                    print(
                                                        f"no project named {deleteproject} was found")
                                                    print("enter a right name")
                                                    deleteproject = input()
                                                else:
                                                    os.system(
                                                        f"cd {user}Projects && rm {deleteproject}.txt")
                                            else:
                                                print(
                                                    "enter the name of the prjoect you want to edit")
                                                editproject = input()
                                                while not f"{editproject}.txt" in os.listdir("/media/lenovo/E/ITI content/python/day3/{user}Projects".format(user=user)):
                                                    print(
                                                        f"no project named {editproject} was found")
                                                    print("enter a right name")
                                                    editproject = input()
                                                else:
                                                    print(
                                                        "enter some details about the project")
                                                    details = input()
                                                    while details == "":
                                                        print(
                                                            "please enter details")
                                                        details = input()
                                                    else:
                                                        print(
                                                            "please enter your predicted target")
                                                        target = input()
                                                        while not target.isnumeric():
                                                            print(
                                                                "please enter a number")
                                                            target = input()
                                                        else:
                                                            edited = open(
                                                                f"{user}Projects/{editproject}.txt", "w")
                                                            edited.write(
                                                                f"--------------------{editproject}--------------------\n details:{details}\n target:{target}\n")
                                                            edited.close()
                                                            print(
                                                                f"Project named {editproject} was edited successfully :)")
                                                            exit()

                        else:
                            create_project_Directory()

                    usersFile.close()
                break
        else:
            print("Invalid email or password")
            logining_in()


logining_in()

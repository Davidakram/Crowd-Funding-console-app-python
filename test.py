import os
# os.chdir("david")

# print(os.listdir("/media/lenovo/E/ITI content/python/day3"))
os.system("ls ")
# os.system("python3 registertion.py")
# user = 'david'
# os.system("mkdir {user}Projects".format(user=user))
# user = 'david'
# projectName = 'test1.py'

# if projectName in os.listdir("/media/lenovo/E/ITI content/python/day3/{user}".format(user=user)):
#     print("Project Directory already exists")
# else:
#     os.system("cd /media/lenovo/E/ITI content/python/day3/{user}Projects".format(
#         user=user) | "touch {projectName}".format(projectName=projectName))


# def create_project_Directory(user):
#     if f"{user}Projects" not in os.listdir():
#         print("hi")
#     else:
#         print("Project Directory already exists")


# create_project_Directory("david")
user = 'david'
projectName = 'test1.py'
os.system(
    f"cd {user} && touch {projectName}.py")

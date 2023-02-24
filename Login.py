import os
import re
import psycopg2

id = ''
dbuser = "postgres"
dbPassword = "david"
dbname = "pythontask"


def create_project():
    os.system("clear")

    print("please enter the project title")
    project_name = input()
    while project_name == "":
        print("Project name cannot be empty")
        print("Please enter a valid project name")
        project_name = input()
    else:
        connect = psycopg2.connect(
            user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
        cursor = connect.cursor()
        query_select_create = f"select projectname from projects where userid='{id}'"
        cursor.execute(query_select_create)
        connect.commit()
        projects = cursor.fetchall()
        for project in projects:
            while project[0] == project_name:
                print("Project name already exists")
                print("Please enter another project name")
                project_name = input()
                while project_name == "":
                    print("Project name cannot be empty")
                    print("Please enter a valid project name")
                    project_name = input()

        print("please enter the project description")
        project_description = input()
        while project_description == "":
            print("Project description cannot be empty")
            print("Please enter a valid project description")
            project_description = input()
        else:
            print("Please enter the project target")
            project_target = input()
            while not project_target.isnumeric():
                print("target must be a number")
                print("Please enter a valid project target")
                project_target = input()
            else:
                try:
                    connect = psycopg2.connect(
                        user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
                    cursor = connect.cursor()
                    query_project_insert = f"insert into projects(userid,projectname,target,projectdescription) values('{id}','{project_name}',{project_target},'{project_description}')"
                    cursor.execute(query_project_insert)
                    connect.commit()
                    cursor.close()
                    connect.close()
                    print(
                        f"Project named {project_name} was created successfully :)")
                    Select_Option()
                except Exception as e:
                    print(e)


def delete_project():
    os.system("clear")

    print("please enter the project name you want to delete")
    project_delete = input()
    while project_delete == "":
        print("Project name cannot be empty")
        print("Please enter a valid project name")
        project_delete = input()
    else:
        connection = psycopg2.connect(
            user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
        dbcursor = connection.cursor()
        query_select_delete = f"select projectname from projects where userid='{id}'"
        dbcursor.execute(query_select_delete)
        connection.commit()
        allprojects = dbcursor.fetchall()
        for project in allprojects:
            if project[0] == project_delete:
                query_delete = f"delete from projects where userid='{id}' and projectname='{project_delete}'"
                dbcursor.execute(query_delete)
                connection.commit()

                print("project was deleted successfully")
                dbcursor.close()
                connection.close()
                Select_Option()
        else:
            print("project not found")
            delete_project()


def view_All_Projects():
    os.system("clear")

    connection = psycopg2.connect(
        user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
    dbcursor = connection.cursor()
    query_view_all_projects = f"select * from projects where userid='{id}'"
    dbcursor.execute(query_view_all_projects)
    connection.commit()
    Projects = dbcursor.fetchall()
    for project in Projects:
        print(project)
    print(f"Total Projects: {len(Projects)}")
    Select_Option()


def update_project():
    os.system("clear")

    print("please enter the project name you want to update")
    project_update = input()
    while project_update == "":
        print("Project name cannot be empty")
        print("Please enter a valid project name")
        project_update = input()
    else:
        connection = psycopg2.connect(
            user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
        dbcursor = connection.cursor()
        query_select_update = f"select projectname from projects where userid='{id}'"
        dbcursor.execute(query_select_update)
        connection.commit()
        projects = dbcursor.fetchall()
        for project in projects:
            if project[0] == project_update:
                print("choose from the following options")
                print("1.update project name")
                print("2.update project target")
                print("3.update project description")
                reply = input()
                while reply != "1" and reply != "2" and reply != "3":
                    print("please choose from the following options(1,2,3)")
                    reply = input()
                else:
                    if reply == "1":
                        print("enter the new project name")
                        new_name = input()
                        while new_name == "":
                            print("Project name cannot be empty")
                            print("Please enter a valid project name")
                            new_name = input()
                        else:
                            for duplicate_project in projects:
                                while duplicate_project[0] == new_name:
                                    print("Project name already exists")
                                    print("Please enter another project name")
                                    new_name = input()
                                    while new_name == "":
                                        print("Project name cannot be empty")
                                        print(
                                            "Please enter a valid project name")
                                        new_name = input()

                            quere_update_project_name = f"update projects set projectname='{new_name}'where userid='{id}' and projectname='{project_update}'"
                            dbcursor.execute(quere_update_project_name)
                            connection.commit()
                            dbcursor.close()
                            connection.close()
                            print("project name updated successfully")
                            Select_Option()
                    elif reply == "2":
                        print("enter the new project target")
                        new_target = input()
                        while not new_target.isnumeric():
                            print("target must be a number")
                            print("Please enter a valid project target")
                            new_target = input()
                        else:
                            query_update_project_target = f"update projects set target='{new_target}' where userid='{id}' and projectname='{project_update}'"
                            dbcursor.execute(query_update_project_target)
                            connection.commit()
                            dbcursor.close()
                            connection.close()
                            print("project target updated successfully")
                            Select_Option()
                    else:
                        print("enter the new project description")
                        new_desc = input()
                        while new_desc == "":
                            print("Project description cannot be empty")
                            print("Please enter a valid project description")
                            new_desc = input()
                        else:
                            quere_update_project_desc = f"update projects set projectdescription='{new_desc}' where userid='{id}' and projectname='{project_update}'"
                            dbcursor.execute(quere_update_project_desc)
                            connection.commit()
                            dbcursor.close()
                            connection.close()
                            print("project description updated successfully")
                            Select_Option()
        else:
            print("project not found")
            update_project()

            # query_update=f"update projects set projectname='{project_update}' where userid='{id}'"


def Select_Option():

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~choose one of the following options~~~~~~~~~~~~~~~~~~~~~~~")
    print("1. Create a new project")
    print("2. View all projects")
    print("3. Delete a project")
    print("4. Update a project")
    print("5.login to another account")
    print("6. Exit")
    reply = input()
    while reply != "1" and reply != "2" and reply != "3" and reply != "4" and reply != "5" and reply != "6":

        print("please enter a valid option")
        reply = input()
    else:
        if reply == "1":
            create_project()
        elif reply == "2":
            view_All_Projects()
        elif reply == "3":
            delete_project()
        elif reply == "4":
            update_project()
        elif reply == "5":
            logining_in()
        else:
            print("Goodbye")
            print("Thank you for using the project manager :)")
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

        connection = psycopg2.connect(
            user=dbuser, password=dbPassword, host="127.0.0.1", port="5432", database=dbname)
        dbcursor = connection.cursor()
        query_select = "select useremail from usersdata "
        dbcursor.execute(query_select)
        connection.commit()

        rec = dbcursor.fetchall()
        for rec in rec:
            if rec[0] == email:
                query_select_id = "select id from usersdata where useremail = '" + \
                    rec[0] + "'"
                dbcursor.execute(query_select_id)
                id_rec = dbcursor.fetchall()
                global id
                id = id_rec[0][0]

                query_select_password = "select userpassword from usersdata where useremail = '" + \
                    rec[0] + "'"
                dbcursor.execute(query_select_password)
                password_rec = dbcursor.fetchall()
                print("please enter your password: ")
                passwd = input()
                while not passwd == password_rec[0][0]:
                    print("wrong password")
                    print("please enter your password again: ")
                    passwd = input()
                else:
                    print("Login Successful")
                    Select_Option()
                    dbcursor.close()
                    connection.close()

                    break

# //////////////////////////////////////////////////
        else:
            print("Invalid email or password")
            logining_in()


logining_in()

from model.user import User
from service.dataService import usersDB
import os

def ask_user():
    print("Insert name:")
    name = input()
    
    print("Insert password:")
    password = input()

    return User(name, password)

def login():
    os.system('cls')
    print("Login!\n\nLeft login name empty to go back.")

    user = ask_user()

    if(not check_user(user)):
        print("User or password is incorrect, register yourself")
        return register()
    else:
        return user.name

def register():
    os.system('cls')
    print("Register!\n\nLeft register name empty to go back.")

    user = ask_user()
   
    if(check_user(user)):
        print("User already exist, log in")
        return login()
    else:
        if(user.name != ""):
            add_user(user)
            print("succesfully logged")
            return login()
        else:
            return login()

def add_user(user):
    usersDB.append(user)

def check_user(user):
    newUsuarios = filter(lambda u: u.name == user.name and u.password == user.password, usersDB)
    return True if len(list(newUsuarios)) > 0 else False
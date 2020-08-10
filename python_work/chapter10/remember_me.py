import json
import os
import sys

path = os.path.join(sys.path[0])

def get_stored_username():
    """Get Stored username if avilable"""
    filename = f"{path}/json_files/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username"""
    username = input("What is your name? ")
    filename = f"{path}/json_files/username.json"
    with open(filename, "w+") as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name"""
    username = get_stored_username()
    confirm = input(f"Are you {username}? (Y/n) ")
    if confirm.lower() == "n":
        username = get_new_username()
    else:
        if username:
            print(f"Welcome back, {username}")
        else:
            username = get_new_username()
            print(f"We will remember you, when you come back {username}")

greet_user()
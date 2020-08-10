import json
import os
import sys

path = os.path.join(sys.path[0])

def get_stored_fav_number():
    # Get favorite number from file
    filename = f"{path}/json_files/fav_num.json"
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_num

def get_new_fav_num():
    # If file doesn't exist, get new number
    fav_num = input("What is your favorite number? ")
    filename = f"{path}/json_files/fav_num.json"
    with open(filename, "w+") as f:
        json.dump(fav_num, f)
    return fav_num

def favorite_number():
    # Get and present person's favorite number
    fav_num = get_stored_fav_number()

    if fav_num:
        print(f"Your favoriter number is {fav_num}.")
    else:
        fav_num = get_new_fav_num()
        print(f"I will always remeber your favorite number now! (Unless you delete the fav_num file in the json_file directory, then I'll forget...)")

favorite_number()
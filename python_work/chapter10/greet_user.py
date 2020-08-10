import json
import os
import sys

path = os.path.join(sys.path[0])
filename = f"{path}/json_files/username.json"

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
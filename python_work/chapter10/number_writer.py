import json
import os
import sys

path = os.path.join(sys.path[0])
filename = path + "/json_files/numbers.json"

numbers = [2, 3, 5, 7, 11, 13]

with open(filename, "w+") as f:
    json.dump(numbers, f)

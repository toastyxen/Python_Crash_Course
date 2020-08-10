import os
import sys

path = os.path.join(sys.path[0])
filename = path + "/text_files/pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
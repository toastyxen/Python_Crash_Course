import os
import sys

path = os.path.join(sys.path[0])
filename = path + "/text_files/pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter you birthday, in form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi, better luck with the next million?")

print(f"{pi_string[:52]}...")
print(len(pi_string))
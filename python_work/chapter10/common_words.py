import os
import sys

path = os.path.join(sys.path[0])
filename = f"{path}/text_files/moby_dick.txt"

try:
    with open(filename, encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    #pass
    print(f"Sorry, the file {filename} does not exist.")
else:
    words = contents.split()
    words_lower = []
    dick_count = 0
    for word in words:
        if word.lower() == "dick":
            dick_count += 1
        
    print(f"The file {filename} has about {dick_count} instances of the word \"dick\" or \"Dick\".")



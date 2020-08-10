import os
import sys

def count_words(filename):
    """" Count aproximate number of words in a file """
    try:
        with open(filename, encoding="utf-8") as f:
            contents = f.read()
    except FileNotFoundError:
        #print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Count the aproximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

path = os.path.join(sys.path[0])
#filename = f"{path}/text_files/alice.txt"
filenames = [f"{path}/text_files/alice.txt", f"{path}/text_files/siddhartha.txt", f"{path}/text_files/moby_dick.txt", f"{path}/text_files/little_women.txt"]

for filename in filenames:
    count_words(filename)
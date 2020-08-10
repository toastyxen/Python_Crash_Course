import os
import sys

path = os.path.join(sys.path[0])
cat_file = f"{path}/text_files/cats.txt"
dog_file = f"{path}/text_files/dogs.txt"


try:
    with open(cat_file, encoding="utf-8") as cats:
        cat_content = cats.read()
    with open(dog_file, encoding="utf-8") as dogs:
        dog_content = dogs.read()
except FileNotFoundError:
    pass
    #print(f"Sorry, the file {cat_file} does not exist.")
else:
    print(f"Conter of {cat_file}, \n{cat_content}")
    print(f"Content of {dog_file}, \n{dog_content}")

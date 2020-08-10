import os
import sys

path = os.path.join(sys.path[0])
filename = path + "/text_files/programming.txt"

flag = False

while flag == False: 
    user_input = input("Please enter something to write to the file: ") # Ask for URL/IP/Any string really to be input 
    #user_input = user_input.strip() # Strip leading and trailing spaces
    #user_input = user_input.replace(" ", "") # Remove any spaces within the string
    correct = input(f"You entered {user_input} is this correct? y/N: ") # Verify the input is correct from user
    # Further input validation could be done, to verify valid URL/IP and not just a random string.
    if correct.lower() == "y":
        flag = True 
    else:
        flag = False

input_string = user_input

with open(filename, "r") as file_object: # Open the file to read line by line to add to list
    lines = file_object.readlines()

line_list = [] # Initiate list to write all entries too
for line in lines:
    line_list.append(line) # Add each entry to this list

if input_string not in line: # Make sure the input isn't already in the DBL
    with open(filename, "a+") as file_object: # If it's not already in the DBL go ahead open the file and append the new entry to it
            file_object.write(f"\n{input_string}")
else: # If it's already in DBL say so
    print("That string is already in the file.")
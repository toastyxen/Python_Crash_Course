def get_formatted_name(first_name, last_name,  middle_name=""):
    """Return a full name, neatly formatter."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

# This is an infinite loop
while True:
    print(f"Please Tell me your name:")

    print(f"(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name.lower() == "q":
        break
    print(f"(enter 'q' at any time to quit)")
    l_name = input("Last Name: ")
    if l_name.lower() == "q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
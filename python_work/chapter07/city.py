prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you have finished. "

while True:
    city = input(prompt)

    if city.lower() == "quit":
        break
    else:
        print(f"I'd love to go to {city.title()}, but I can't becuase I'm a program, no opposable thumbs, *sad face emote*")
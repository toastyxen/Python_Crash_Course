def describe_pet(animal_type, pet_name):
    """Display information about pet"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet("snake", "JoJo")
describe_pet("gecko", "echo")
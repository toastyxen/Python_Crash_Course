# Store information about pizza being ordered
pizza = {
    "crust": "thicc",
    "toppings": ["mushroom", "extra cheese"],
    }
# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")
for topping in pizza["toppings"]:
    print("\t" + topping)
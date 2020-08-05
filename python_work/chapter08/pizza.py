def make_pizza(crust, size, *toppings):
    """Summerize the pizza we're about to make"""
    print(f"\nMaking a {size}-inch {crust}-crust, pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
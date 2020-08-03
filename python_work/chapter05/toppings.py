topping_amount = input("How many toppings do you want on your pizza? ")
topping_list = []

avilable_toppings = ["pepperoni", "mushroom", "anchovies", "olives", "green peppers", "pineapple", "ham", "sausage", "bacon", "extra cheese"]

if topping_amount == "":
    plain_pizza = input("Are you sure you want a plain pizza? Y/n " )
    if plain_pizza.upper() == "Y":
        print("Your pizza is done.")
        exit()
    elif plain_pizza.upper() == "N":
        topping_amount = input("How many toppings do you want on your pizza? ")
    else:
        print("Okay bye bye!")
        exit()
    
for i in range(int(topping_amount)):
    topping = input("Topping number " + str(i+1) + " ")
    topping_list.append(topping)

for topping in topping_list:
    if topping.lower() not in avilable_toppings:
        print("Sorry we do not have " + topping)
    else:
        print("Adding " + topping + ".")

print("\nFinished making your pizza!")
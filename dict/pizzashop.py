menu = {
    "Cheese": {"ingredients": {"Cheese": 3, "Dough": 5, "Sauce": 2}},
    "Pepperoni": {"ingredients": {"Pepperoni": 3}},
    "Veggie": {"ingredients": {"Veggie": 1}},
}


# with a nested dictionary you can use
def displayMenu():
    # pizza is deined as all the pizza names in menu aka each item in menu dictonary
    # details is the value pair infomration (in this case ingredients) however you dont have acess to the content within in, just the fact that the
    # the value pair a dictornary
    base_price = sum(
        menu["Cheese"]["ingredients"].values()
    )  # the base price of the pizza takes the summation of
    base_ingredients = ", ".join(menu["Cheese"]["ingredients"].keys()) + ", "
    total = 0
    order_num = 1
    print("Menu for Celine's Pizza Shop!")
    for pizza, details in menu.items():
        print(f"{order_num}: {pizza}")
        ingredients_list = (
            base_ingredients + ", ".join(details["ingredients"].keys())
            if pizza != "Cheese"
            else base_ingredients
        )

        print(f"Ingredients: {ingredients_list}")
        total = (
            base_price + sum(details["ingredients"].values())
            if pizza != "Cheese"
            else base_price
        )
        order_num += 1
        print(total)


def order(order_number):
    if order_number == 1:
        print("Cheese Coming Right Up!")
    elif order_number == 2:
        print("Pepperoni Coming Right Up!")
    elif order_number == 3:
        print("Veggie Coming Right Up!")
    else:
        print("Not a Valid order")


displayMenu()
order_number = int(
    input(
        "What Would You like to order? Input 1 for Cheese, 2 for Pepperoni, 3 for Veggie "
    )
)
order(order_number)

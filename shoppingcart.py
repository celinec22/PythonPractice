cart = {}


# Add item to cart, but prevent price updates if item already exists
def add_to_cart(item, price, quantity=1, set_price=False):
    # If item exists, update quantity, but only update price if set_price is True
    if item in cart:
        cart[item]["quantity"] += quantity
        if set_price:  # Only update price if explicitly allowed
            cart[item]["price"] = price
    else:
        cart[item] = {
            "price": price,
            "quantity": quantity,
        }  # ✅ Store as a dictionary, not a tuple


# Function to calculate total price
def calculate_total():
    total = 0
    for item, details in cart.items():
        total += (
            details["price"] * details["quantity"]
        )  # ✅ details is a dictionary, so this works
    return total


# Test cases
add_to_cart("Apple", 0.5, 3)
add_to_cart("Banana", 0.3, 2)
add_to_cart("Apple", 0.8, 1)
add_to_cart("Apple", 1.0, 1, set_price=True)

print(f"Total: ${calculate_total()}")
print(cart)

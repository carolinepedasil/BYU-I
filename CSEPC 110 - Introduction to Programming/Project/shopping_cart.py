# In addition to the required features, I have added the ability to store and display the quantity of each item. 
# The total is calculated based on both the price and quantity, and the output is aligned neatly.

shopping_cart_names = []
shopping_cart_prices = []
shopping_cart_quantities = []

def display_menu():
    print("\nPlease select one of the following: ")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

def add_item():
    item = input("What item would you like to add? ")
    price = float(input(f"What is the price of '{item}'? $"))
    quantity = int(input(f"How many of '{item}' would you like to add? "))
    
    shopping_cart_names.append(item)
    shopping_cart_prices.append(price)
    shopping_cart_quantities.append(quantity)
    
    print(f"'{item}' has been added to the cart.")

def view_cart():
    if len(shopping_cart_names) == 0:
        print("\nThe shopping cart is empty.")
    else:
        print("\nThe contents of the shopping cart are:")
        print(f"{'No.':<5}{'Item':<15}{'Price':<10}{'Quantity':<10}")
        print("-" * 40)
        for i in range(len(shopping_cart_names)):
            print(f"{i + 1:<5}{shopping_cart_names[i]:<15}${shopping_cart_prices[i]:<10.2f}{shopping_cart_quantities[i]:<10}")

def remove_item():
    if len(shopping_cart_names) == 0:
        print("\nThe shopping cart is empty.")
    else:
        view_cart()
        try:
            index = int(input("Which item would you like to remove? Enter the item number: ")) - 1
            if 0 <= index < len(shopping_cart_names):
                removed_item = shopping_cart_names.pop(index)
                shopping_cart_prices.pop(index)
                shopping_cart_quantities.pop(index)
                print(f"'{removed_item}' has been removed from the cart.")
            else:
                print("Sorry, that is not a valid item number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def compute_total():
    if len(shopping_cart_prices) == 0:
        print("\nThe shopping cart is empty.")
    else:
        total = 0
        for i in range(len(shopping_cart_prices)):
            total += shopping_cart_prices[i] * shopping_cart_quantities[i]
        print(f"\nThe total price of the items in the shopping cart is: ${total:.2f}")

print("Welcome to the Shopping Cart Program!")
while True:
    display_menu()
    action = input("Please enter an action: ")

    if action == "1":
        add_item()
    elif action == "2":
        view_cart()
    elif action == "3":
        remove_item()
    elif action == "4":
        compute_total()
    elif action == "5":
        print("Thank you. Goodbye.")
        break
    else:
        print("Invalid input. Please try again.")

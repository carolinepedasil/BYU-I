# This program calculates the total cost of a meal, including sales tax, optional drinks, appetizers, and tip percentage.
# It also calculates the change based on the payment amount entered by the user.

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
number_of_children = int(input("How many children are there? "))
number_of_adults = int(input("How many adults are there? "))

meal_subtotal = (child_meal_price * number_of_children) + (adult_meal_price * number_of_adults)

# Asking if the user wants drinks and appetizers
add_drinks = input("Would you like to add drinks? (yes/no): ").lower()
if add_drinks == "yes":
    drinks_price = float(input("What is the total price of the drinks? "))
else:
    drinks_price = 0.0

add_appetizers = input("Would you like to add appetizers? (yes/no): ").lower()
if add_appetizers == "yes":
    appetizers_price = float(input("What is the total price of the appetizers? "))
else:
    appetizers_price = 0.0

subtotal = meal_subtotal + drinks_price + appetizers_price
print(f"Subtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("What is the sales tax rate? "))

sales_tax = subtotal * (sales_tax_rate / 100)
print(f"Sales Tax: ${sales_tax:.2f}")

total_before_tip = subtotal + sales_tax
print(f"Total (before tip): ${total_before_tip:.2f}")

# Asking for tip percentage
tip_percentage = float(input("What percentage tip would you like to leave? "))
tip = total_before_tip * (tip_percentage / 100)
print(f"Tip: ${tip:.2f}")

final_total = total_before_tip + tip
print(f"Final Total (with tip): ${final_total:.2f}")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - final_total

print(f"Change: ${change:.2f}")

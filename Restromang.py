# Define the menu of the restaurant
menu = { 
    'pizza': 40,
    'pasta': 50,
    'burger': 60,
    'salad': 70,
    'cofee': 80, 
}

print("Welcome to Aditi's Restaurant")
print("Menu:")
print("pizza : Rs 40 \n pasta : Rs 50 \n burger : Rs 60 \n salad : Rs 70 \n cofee : Rs 80")


order_total = 0     #user enter prize added on this var suppose salad then cofee 70+80=150

# First item
item_1 = input("Enter the name of the item you want to order: ")    #check conditions the choice entered by user is available
                                                              #in our restaurent or not if yes then go further if not then 
                                                              #it should display not available  

# Check if item_1 is available
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available yet!")

# Ask if user wants to add another item
another_order = input("Do you want to add another item? (yes/no): ")

if another_order == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:      #membership operator we use here to check users input avalable or not

        order_total += menu[item_2]
        print(f"Item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available!")

# Show total bill
print(f"\nThe total amount of items to pay is Rs {order_total}")

# Payment method selection
payment_method = input("Choose a payment method (cash/online): ")

if payment_method == "cash" or payment_method == "online":
    print("Payment done successfully. Thank you! Visit again.")
else:
    print("Invalid payment method. Please try again or contact staff.")

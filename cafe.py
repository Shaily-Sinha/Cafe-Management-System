from datetime import datetime


# ==========================================
#          CAFE MANAGEMENT SYSTEM
# ==========================================


# Cafe Menu
menu = {
    "Coffee": 80,
    "Tea": 40,
    "Burger": 120,
    "Sandwich": 100,
    "Pasta": 150,
    "Pizza": 200
}


# Stores customer's current order
order = {}


# ------------------------------------------
# Display Cafe Menu
# ------------------------------------------

def display_menu():

    print("\n========== CAFE MENU ==========")

    for index, (item, price) in enumerate(menu.items(), start=1):
        print(f"{index}. {item:<15} Rs.{price}")

    print("===============================")


# ------------------------------------------
# Place Order
# ------------------------------------------

def place_order():

    display_menu()

    while True:

        try:
            item_number = int(input("\nEnter item number: "))

            if item_number < 1 or item_number > len(menu):
                print("Invalid item number. Please try again.")
                continue

            item = list(menu.keys())[item_number - 1]

            quantity = int(input(f"Enter quantity for {item}: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity

            print(f"{quantity} x {item} added to your order.")

            while True:

                more = input(
                    "\nWould you like to order anything else? (y/n): "
                ).strip().lower()

                if more == "y":
                    break

                elif more == "n":
                    print("\nOrder placed successfully!")
                    view_order()
                    return

                else:
                    print("Please enter y or n.")

        except ValueError:
            print("Please enter a valid number.")


# ------------------------------------------
# View Current Order
# ------------------------------------------

def view_order():

    if not order:
        print("\nYour order is currently empty.")
        return

    print("\n========== CURRENT ORDER ==========")

    total = 0

    for index, (item, quantity) in enumerate(order.items(), start=1):

        price = menu[item]
        item_total = price * quantity
        total += item_total

        print(
            f"{index}. {item:<12} "
            f"{quantity} x Rs.{price:<5} "
            f"= Rs.{item_total}"
        )

    print("-----------------------------------")
    print(f"Current Total: Rs.{total}")
    print("===================================")


# ------------------------------------------
# Update Item Quantity
# ------------------------------------------

def update_item():

    if not order:
        print("\nYour order is empty.")
        return

    view_order()

    try:
        item_number = int(
            input("\nEnter item number to update: ")
        )

        if item_number < 1 or item_number > len(order):
            print("Invalid item number.")
            return

        item = list(order.keys())[item_number - 1]

        quantity = int(
            input(f"Enter new quantity for {item}: ")
        )

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        order[item] = quantity

        print(f"{item} quantity updated to {quantity}.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# Remove Item
# ------------------------------------------

def remove_item():

    if not order:
        print("\nYour order is empty.")
        return

    view_order()

    try:
        item_number = int(
            input("\nEnter item number to remove: ")
        )

        if item_number < 1 or item_number > len(order):
            print("Invalid item number.")
            return

        item = list(order.keys())[item_number - 1]

        del order[item]

        print(f"{item} removed from your order.")

    except ValueError:
        print("Please enter a valid number.")


# ------------------------------------------
# Generate Final Bill
# ------------------------------------------

def generate_bill():

    if not order:
        print("\nCannot generate bill because your order is empty.")
        return

    # Customer details
    customer_name = input("\nEnter customer name: ").strip()

    if not customer_name:
        customer_name = "Guest"

    # Current date and time
    now = datetime.now()

    date = now.strftime("%d-%m-%Y")
    time = now.strftime("%I:%M %p")

    # Bill number
    bill_number = now.strftime("%H%M%S")

    print("\n==================================================")
    print("                 BREW & BITE CAFE")
    print("              Dehradun, Uttarakhand")
    print("==================================================")

    print(f"Bill No. : {bill_number}")
    print(f"Customer : {customer_name}")
    print(f"Date     : {date}")
    print(f"Time     : {time}")

    print("--------------------------------------------------")
    print(f"{'Item':<18}{'Qty':<8}{'Price':<12}{'Amount':<10}")
    print("--------------------------------------------------")

    subtotal = 0

    for item, quantity in order.items():

        price = menu[item]
        item_total = price * quantity

        subtotal += item_total

        print(
            f"{item:<18}"
            f"{quantity:<8}"
            f"Rs.{price:<9}"
            f"Rs.{item_total}"
        )

    # Tax calculation
    gst_rate = 5
    gst = subtotal * gst_rate / 100

    grand_total = subtotal + gst

    print("--------------------------------------------------")

    print(f"{'Subtotal:':<38}Rs.{subtotal:.2f}")
    print(f"{'GST (5%):':<38}Rs.{gst:.2f}")

    print("--------------------------------------------------")

    print(f"{'TOTAL:':<38}Rs.{grand_total:.2f}")

    print("==================================================")
    print("              Thank You! Visit Again!")
    print("==================================================")


# ------------------------------------------
# Main Program
# ------------------------------------------

def main():

    while True:

        print("\n================================")
        print("     CAFE MANAGEMENT SYSTEM")
        print("================================")

        print("1. View Menu")
        print("2. Place Order")
        print("3. View Current Order")
        print("4. Update Item Quantity")
        print("5. Remove Item")
        print("6. Generate Bill")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            place_order()

        elif choice == "3":
            view_order()

        elif choice == "4":
            update_item()

        elif choice == "5":
            remove_item()

        elif choice == "6":
            generate_bill()

        elif choice == "7":
            print("\nThank you for using Cafe Management System!")
            break

        else:
            print(
                "\nInvalid choice. "
                "Please enter a number from 1 to 7."
            )


# ------------------------------------------
# Start Program
# ------------------------------------------

if __name__ == "__main__":
    main()
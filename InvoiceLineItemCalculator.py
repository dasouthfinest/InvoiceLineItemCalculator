# O’Tria Fee
# CIS 261
# Lab: Invoice Line Item Calculator

def get_price():
    """Get and validate a price from user input"""
    while True:
        value = input("Enter price: ")
        try:
            price = float(value)   # decimal value needed here
            if price > 0:
                return price
            else:
                print("Invalid decimal number. Please try again.")
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    """Get and validate a quantity from user input"""
    while True:
        value = input("Enter quantity: ")
        try:
            qty = int(value)
            if qty > 0:
                return qty
            else:
                print("Invalid integer. Please try again.")
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity

        print(f"\nPRICE: {price:.2f}")
        print(f"QUANTITY: {quantity}")
        print(f"TOTAL: {total:.2f}")

        again = input("Enter another line item? (y/n): ").strip().lower()
        if again != "y":
            break
        print()

    print()
    print("Bye!")

if __name__ == "__main__":
    main()

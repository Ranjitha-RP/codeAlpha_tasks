#defining the dictionary
stock_data = {
    "aapl": {
        "company": "Apple Inc",
        "price": 180,
        "sector": "Technology"
    },
    "tsla": {
        "company": "Tesla Inc",
        "price": 250,
        "sector": "Automobile"
    },
    "googl": {
        "company": "Alphabet Inc",
        "price": 140,
        "sector": "Technology"
    },
    "amzn": {
        "company": "Amazon Inc",
        "price": 155,
        "sector": "E-commerce"
    }
}
# User input
stock_name = input("Enter stock name (aapl/tsla/googl/amzn): ").lower()
quantity = int(input("Enter quantity: "))

# Check stock availability
if stock_name in stock_data:
    stock = stock_data[stock_name]
    total = stock["price"] * quantity

    # Display details
    print("\nCompany:", stock["company"])
    print("Sector:", stock["sector"])
    print("Price per Stock:", stock["price"])
    print("Quantity:", quantity)
    print("Total Investment Value:", total)

    # Optional file save
    save = input("\nSave to file? (yes/no): ").lower()
    if save == "yes":
        with open("investment.txt", "a") as file:
            file.write(
                f"{stock['company']} | "
                f"Sector: {stock['sector']} | "
                f"Qty: {quantity} | "
                f"Total: {total}\n"
            )
        print("Saved successfully!")

else:
    print("Stock not found!")
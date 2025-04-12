def main():
    # Fruit prices in dollars
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    # Ask user how many of each fruit they want
    for fruit_name, price in fruits.items():
        try:
            amount = int(input(f"How many ({fruit_name}) do you want?: "))
            total_cost += price * amount
        except ValueError:
            print("Please enter a valid number. We'll count that as 0.")
    
    # Show the total cost formatted to two decimal places
    print(f"\nYour total is ${total_cost:.2f}")


# Required Python boilerplate
if __name__ == '__main__':
    main()

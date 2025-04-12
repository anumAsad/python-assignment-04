def main():
    try:
        # Get user input for dividend
        dividend: int = int(input("Please enter an integer to be divided: "))
        
        # Get user input for divisor
        divisor: int = int(input("Please enter an integer to divide by: "))

        # Handle division by zero
        if divisor == 0:
            print("Error: Division by zero is not allowed.")
            return

        # Perform integer division and get remainder
        quotient: int = dividend // divisor
        remainder: int = dividend % divisor

        # Display result using formatted output
        print(f"The result of this division is {quotient} with a remainder of {remainder}")

    except ValueError:
        print("Invalid input! Please enter integers only.")

# Required to call the main function
if __name__ == '__main__':
    main()

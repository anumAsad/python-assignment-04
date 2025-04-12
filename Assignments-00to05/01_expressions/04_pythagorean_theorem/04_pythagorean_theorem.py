import math  # Import math library for sqrt function

def main():
    try:
        ab: float = float(input("Enter the length of AB: "))
        ac: float = float(input("Enter the length of AC: "))

        # Validate inputs (sides must be positive)
        if ab <= 0 or ac <= 0:
            print("Side lengths must be positive numbers.")
            return

        # Calculate the hypotenuse
        bc: float = math.sqrt(ab**2 + ac**2)
        
        # Print result with formatted output
        print(f"The length of BC (the hypotenuse) is: {bc:.2f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Required to call the main function
if __name__ == '__main__':
    main()

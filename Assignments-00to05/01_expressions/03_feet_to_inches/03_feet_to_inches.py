"""
Program to convert feet to inches.
"""

INCHES_IN_FOOT: int = 12  # Conversion factor

def main():
    try:
        feet: float = float(input("Enter number of feet: "))  # Get input and convert to float
        if feet < 0:
            print("Please enter a non-negative value.")
            return

        inches: float = feet * INCHES_IN_FOOT  # Perform conversion
        unit = "inch" if inches == 1 else "inches"  # Handle singular/plural
        print(f"That is {inches} {unit}!")  # Formatted output
    
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Required to call the main function
if __name__ == '__main__':
    main()

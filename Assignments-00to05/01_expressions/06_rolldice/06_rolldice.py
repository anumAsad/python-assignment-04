"""
Simulate rolling two dice, print results of each roll, and display the total.
"""
import random  # Import random library for generating random numbers

def roll_dice(num_sides: int = 6):
    """Simulate rolling a single die with 'num_sides' sides."""
    return random.randint(1, num_sides)

def main():
    try:
        num_sides: int = int(input("Enter the number of sides on each die (default is 6): ") or 6)

        while True:
            die1 = roll_dice(num_sides)
            die2 = roll_dice(num_sides)
            total = die1 + die2

            print(f"\nRolling two {num_sides}-sided dice...")
            print(f"First die: {die1}")
            print(f"Second die: {die2}")
            print(f"Total of two dice: {total}")

            # Ask user if they want to roll again
            again = input("\nRoll again? (yes/no): ").strip().lower()
            if again not in ("yes", "y"):
                print("Thanks for playing! 🎲")
                break

    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Required to call the main function
if __name__ == '__main__':
    main()

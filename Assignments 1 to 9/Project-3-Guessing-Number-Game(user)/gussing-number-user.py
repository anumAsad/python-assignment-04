import random

def computer_guess():
    print("🤖 Welcome to the Computer Guessing Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it!")

    low, high = 1, 100  # Define the range
    attempts = 0  # Count the number of guesses
    
    input("Press Enter when you're ready...")  # Give time for the user to think of a number

    while True:
        guess = random.randint(low, high)  # Computer makes a guess
        attempts += 1

        print(f"\nIs your number {guess}? 🤔")
        user_feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if user_feedback == 'h':
            high = guess - 1  # Adjust the high end of the range
        elif user_feedback == 'l':
            low = guess + 1  # Adjust the low end of the range
        elif user_feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts!")
            break  # Stop the loop when the number is found
        else:
            print("⚠️ Invalid input! Please enter 'h', 'l', or 'c'.")

if __name__ == "__main__":
    computer_guess()
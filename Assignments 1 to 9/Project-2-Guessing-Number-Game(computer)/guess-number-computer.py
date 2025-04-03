import random  

def guess_the_number():
    print("🎯 Welcome to the Guess the Number Game! 🎯")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    
    attempts = 0  # Track the number of attempts
    
    while True:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count
            
            # Check if the guess is correct
            if guess < secret_number:
                print("Too low! Try again. ⬆️")
            elif guess > secret_number:
                print("Too high! Try again. ⬇️")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit loop when guessed correctly
        except ValueError:
            print("⚠️ Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_the_number()

import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_user_choice():
    while True:
        choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        print("⚠️ Invalid choice! Please enter Rock, Paper, or Scissors.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie! 🤝"
    
    winning_combos = {
        "rock": "scissors",  # Rock beats Scissors
        "scissors": "paper",  # Scissors beat Paper
        "paper": "rock"  # Paper beats Rock
    }

    if winning_combos[user_choice] == computer_choice:
        return f"You win! 🎉 {user_choice.capitalize()} beats {computer_choice.capitalize()}!"
    else:
        return f"You lose! 😢 {computer_choice.capitalize()} beats {user_choice.capitalize()}!"

def play():
    print("✂️ Welcome to Rock, Paper, Scissors! 🪨📄")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\n🧑 You chose: {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")
        
        print(determine_winner(user_choice, computer_choice))
        
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    play()

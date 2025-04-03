import random

# List of words for the game
word_list = ["python", "developer", "hangman", "keyboard", "programming"]

# Function to choose a random word
def get_random_word():
    return random.choice(word_list)

# Function to display the current word progress
def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Main Hangman function
def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Maximum wrong guesses

    print("\n🎭 Welcome to Hangman! Try to guess the word.")

    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"❌ Wrong attempts left: {attempts}")
        print(f"📝 Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        guess = input("🔠 Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter!")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
        else:
            print("❌ Incorrect guess!")
            attempts -= 1

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            return
        
    print("\n💀 You lost! The word was:", word.upper())

if __name__ == "__main__":
    play_hangman()

import random
import string

def generate_password(length, use_numbers, use_symbols):
    letters = string.ascii_letters  # A-Z, a-z
    numbers = string.digits if use_numbers else ""
    symbols = string.punctuation if use_symbols else ""
    
    all_chars = letters + numbers + symbols
    if not all_chars:
        print("Error: You must select at least one character type.")
        return None
    
    return "".join(random.choice(all_chars) for _ in range(length))

def main():
    print("🔒 Welcome to the Password Generator!")
    
    length = int(input("Enter password length: "))
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

    password = generate_password(length, use_numbers, use_symbols)
    
    if password:
        print(f"\nYour secure password: {password}")

if __name__ == "__main__":
    main()

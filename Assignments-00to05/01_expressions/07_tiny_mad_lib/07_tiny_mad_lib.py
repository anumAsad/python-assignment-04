SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
    # Get inputs from the user
    adjective: str = input("Please type an adjective and press enter: ").strip()
    noun: str = input("Please type a noun and press enter: ").strip()
    verb: str = input("Please type a verb and press enter: ").strip()

    # Print the formatted sentence
    print(f"{SENTENCE_START} {adjective} {noun} {verb}!")

# Call main function
if __name__ == '__main__':
    main()

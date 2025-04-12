def read_phone_numbers():
    """
    Ask the user for names/numbers to store in a phonebook (dictionary).
    Returns the filled phonebook.
    """
    phonebook = {}  # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Print out all the names and numbers in the phonebook.
    """
    print("\nPhonebook entries:")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    """
    Allow the user to look up phone numbers by name.
    If name exists, show the number; otherwise inform the user.
    """
    print("\nPhonebook Lookup:")
    while True:
        name = input("Enter name to lookup (or press Enter to quit): ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Required Python boilerplate
if __name__ == '__main__':
    main()

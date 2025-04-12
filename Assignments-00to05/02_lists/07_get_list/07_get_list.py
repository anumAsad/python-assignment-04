def main():
    lst = []  # Make an empty list to store values

    val = input("Enter a value: ")  # Prompt for the first input
    while val:  # Keep looping until the user enters an empty string
        lst.append(val)
        val = input("Enter a value: ")  # Prompt again

    print("Here's the list:", lst)


# This line ensures main() runs when the script is executed
if __name__ == '__main__':
    main()

def main():
    print("Welcome to Mad Libs! Fill in the blanks to create a funny story.\n")

    # Get user inputs
    place = input("Enter a place: ")
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")

    # Create the Mad Libs story using f-strings
    story = f"Today, I went to the {place}. It was very {adjective}! I saw a {noun} that could {verb}."

    # Print the final story
    print("\nHere's your Mad Libs story:")
    print(story)


if __name__ == "__main__":
    main()

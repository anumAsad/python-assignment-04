def get_user_numbers():
    """
    Prompt the user to enter numbers one by one.
    Return a list of numbers once the user enters a blank line.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    return user_numbers


def count_nums(num_lst):
    """
    Count how many times each number appears in the list.
    Return a dictionary where keys are numbers and values are their counts.
    """
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict


def print_counts(num_dict):
    """
    Print how many times each number appeared.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


if __name__ == '__main__':
    main()

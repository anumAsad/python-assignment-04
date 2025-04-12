def get_last_element(lst):
    """
    Prints the last element of the provided list.
    """
    # Option 1: Using index based on length
    print(lst[len(lst) - 1])
    
    # Option 2 (cleaner and preferred in Python):
    # print(lst[-1])  # <- Also works!


# No need to edit below this line

def get_lst():
    """
    Prompts the user to enter one element of the list at a time 
    and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst


def main():
    lst = get_lst()
    get_last_element(lst)


if __name__ == '__main__':
    main()

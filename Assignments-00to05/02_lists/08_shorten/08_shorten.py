MAX_LENGTH: int = 3

def shorten(lst):
    """
    Removes items from the end of the list until its length is MAX_LENGTH.
    Prints each item removed.
    """
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)


# No need to edit code beyond this point

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop: ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)


if __name__ == '__main__':
    main()

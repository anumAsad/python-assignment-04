def add_many_numbers(numbers: list[int]) -> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """
    return sum(numbers)  # More efficient and cleaner

def main():
    # Static list (existing approach)
    numbers: list[int] = [1, 2, 3, 4, 5]
    
    # Alternatively, allow user input
    # numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

    sum_of_numbers: int = add_many_numbers(numbers)  # Get sum
    print(f"Sum of numbers: {sum_of_numbers}")  # Print sum

if __name__ == '__main__':
    main()

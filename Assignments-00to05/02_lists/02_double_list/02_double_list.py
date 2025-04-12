def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers
    
    # Using list comprehension to double each element
    numbers = [x * 2 for x in numbers]
    
    print(numbers)  # Print the doubled list

if __name__ == '__main__':
    main()

def main():
    # Assigning ages based on the problem statement
    anton: int = 21  # Anton is 21 years old
    beth: int = anton + 6  # Beth is 6 years older than Anton
    chen: int = beth + 20  # Chen is 20 years older than Beth
    drew: int = chen + anton  # Drew is as old as Chen's age plus Anton's age
    ethan: int = chen  # Ethan is the same age as Chen

    # Printing the results
    print("Anton is", anton)
    print("Beth is", beth)
    print("Chen is", chen)
    print("Drew is", drew)
    print("Ethan is", ethan)


# Ensures main() runs when script is executed
if __name__ == '__main__':
    main()

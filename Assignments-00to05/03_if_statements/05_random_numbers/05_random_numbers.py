import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=" ")
    print()  # for a newline after all numbers are printed


if __name__ == '__main__':
    main()

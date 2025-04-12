def main():
    # Prompt user for temperature input in Fahrenheit
    degrees_fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Display the converted temperature
    print(f"Temperature: {degrees_fahrenheit:.1f}F = {degrees_celsius:.6f}C")


# Ensures main() runs when script is executed
if __name__ == '__main__':
    main()

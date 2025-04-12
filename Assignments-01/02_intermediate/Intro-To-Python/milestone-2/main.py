"""
Prompts the user for a weight on Earth
and a planet (in separate inputs). Then 
prints the equivalent weight on that planet.
"""

# Gravity constants relative to Earth
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Prompt the user for their Earth weight
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    # Determine gravity constant for the given planet
    if planet == "Mercury":
        gravity = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity = VENUS_GRAVITY
    elif planet == "Mars":
        gravity = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity = URANUS_GRAVITY
    elif planet == "Neptune":
        gravity = NEPTUNE_GRAVITY
    else:
        print("Invalid planet.")
        return

    # Calculate and print the result
    weight_on_planet = earth_weight * gravity
    rounded_weight = round(weight_on_planet, 2)
    print("The equivalent weight on " + planet + ": " + str(rounded_weight))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# Created By: Bryson
# Date: 10 13, 2026
# This program asks the user for the side length of a Octagon
# and then calculates the area and perimeter.

import math


def main():

    # Get the side length from the user and convert to float
    L = float(
        input(
            "Hello, welcome to Brysons Octagon Area and Perimeter calculator! Enter the side length (cm):"
        )
    )

    # Calculate the Perimeter of the Octagon
    Perimeter = 8 * L

    # Calculate the area of the Octagon
    Area = 2 * (1 + math.sqrt(2)) * L ** 2

    # Display the Perimeter and Area to the user
    print("The Perimeter of the Octagon is: {:.2f} cm".format(Perimeter))
    print("The Area of the Octagon is: {:.2f} cm²".format(Area))


if __name__ == "__main__":
    main()

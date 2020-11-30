#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This program is the number guessing game

import constants


def main():
    # this function can tell the user if the number they guessed is correct

    # input
    guessed_number = int(input("Guess a number between 0 to 9: "))
    print("")

    # process
    if guessed_number == constants.NUMBER:
        # output
        print("You are correct!! {} is the correct number."
              .format(guessed_number))

    # process
    if guessed_number != constants.NUMBER:
        # output
        print("You are wrong! Try again")


if __name__ == "__main__":
    main()

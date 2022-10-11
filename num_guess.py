#!/usr/bin/env python3
# Created by: Katie G
# Created on: October 10th, 2022
# This program makes the user guess
# the number that I have inputted.
# The program will tell the user if
# they got it right or wrong.
import num_guess_constants


# this function gets the user's guess and
# checks to see if it is the correct num.
# The function then displays the result
# to the user.
def main():
    # getting the user's guess.
    user_guess = int(
        input("Guess my favorite number from 0 - 9 :) I bet you won't get it :) ")
    )

    # check to see if user guess is correct.
    if user_guess == num_guess_constants.CORRECT_NUM:
        print("You got it right :) Good job :)")

    # check to see if user guess is not correct.
    if user_guess != num_guess_constants.CORRECT_NUM:
        print("You did not get it right :( I am sad now :(")


if __name__ == "__main__":
    main()

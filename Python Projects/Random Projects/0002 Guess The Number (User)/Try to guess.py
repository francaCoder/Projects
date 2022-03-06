
from random import randint


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "C":
        if low != high:
            guess = randint(low, high)
        else:
            guess = low # Could also be high b/c low = high
        feedback = input(f"is {guess} too high [H], too low [L], or correctly [C] ").upper()
        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1

    print(f"Yay, the computer guessed your number, {guess} correctly!")


computer_guess(1000)
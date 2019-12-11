# CMPT 120 Intro to Programming
# Lab #5 – Conditional Execution and Strings
# Author: Thomas Magnusson
# Created: 2019-10-28

# This lab is not suitable for testing, lots of input, lots of control statements.
# Significant refactoring would need to be made to make this sufficiently testable.

def main():
    animal = 'dog'.lower()
    while True:
        print("I'm thinking of an animal... (type a word that starts with 'q' to quit)")
        guess = input('Take a guess: ').lower()
        if guess[0] == 'q':
            print('Bye.')
            return
        elif guess == animal:
            does_like_animal = input("Do you like this animal? ('y' or 'n')").lower()
            if(does_like_animal[0] == 'y'):
                print("That's great!")
            else:
                print("A cat person, I see.")
            break
        else:
            print(f"Nope, not a {guess}. Try again.")
    print(f'Congrats! You won, {animal} was the animal!')

if __name__ == '__main__':
    main()
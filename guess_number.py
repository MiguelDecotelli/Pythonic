import sys
from random import randint


def main():
    number = level()
    hunch = guess()

    if hunch < number:
        print("Too small!")
    elif hunch > number:
        print("Too large!")
    else:
        print("Just right!")
        sys.exit()



def level():
    while True:
        try:
            n = int(input("Level: "))
            print(n)
            number = randint(1, n)
            if n >= 1:
                return number
        except ValueError:
            pass


def guess():
    while True:
        try:
            hunch = int(input("Guess: "))
            if hunch >= 1:
                return hunch
        except (ValueError, TypeError):
            pass

if __name__ == '__main__':
    main()

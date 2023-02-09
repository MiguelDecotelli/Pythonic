import random

def main():
    level = get_level()
    math_problems = 0
    score = 0
    tries = 2

    while math_problems < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            result = int(input(f"{x} + {y} = "))
            if x + y == result:
                score += 1
            elif x + y != result:
                while tries > 0:
                    print("EEE")
                    tries -= 1
                    result = int(input(f"{x} + {y} = "))
                    if tries == 0:
                        print(f"{x} + {y} = {x + y}")
                    continue
            math_problems += 1
        except ValueError:
            pass
        print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if 0 < n <= 3:
                return n
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        integer = random.randrange(10)
        return integer

    elif level == 2:
        integer = random.randrange(10, 100)
        return integer

    elif level == 3:
        integer = random.randrange(100, 1000)
        return integer
    else:
        raise ValueError

if __name__ == "__main__":
    main()
import sys

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)

    if not sys.argv[1][-3:] == ".py":
        print("Not a Python file")
        sys.exit(1)

    print(count_lines())

def count_lines():
    lines = 0

    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.isspace() == True or line.lstrip().startswith('#') == True:
                    continue
                else:
                    lines += 1
    except FileNotFoundError:
        print("File does not exist")
        sys.exit(1)
    return lines


if __name__ == '__main__':
    main()
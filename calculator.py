def main():
    math = input("Do the math: ")
    print(f"{convert(math):.2f}")

def convert(math):
        if "+" in math:
            x, y = math.split("+")
            return int(x) + int(y)
        elif "-" in math:
            x, y = math.split("-")
            return int(x) - int(y)
        elif "*" in math:
            x, y = math.split("*")
            return int(x) * int(y)
        elif "/" in math:
            x, y = math.split("/")
            return int(x) / int(y)

if __name__ == '__main__':            
    main()
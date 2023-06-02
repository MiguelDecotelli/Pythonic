def main():
    fraction = input("Fraction: ")
    while True:
        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            fraction = input("Fraction: ")


def convert(fraction):
    while True:
        try:
            x, y = fraction.split("/")
            percentage = int(x) / int(y)
        except (ValueError, ZeroDivisionError):
            raise
        if int(x) <= int(y):
            percentage = int(x) / int(y)
            return round(percentage * 100)
        else:
            fraction = input("Fraction: ")

def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
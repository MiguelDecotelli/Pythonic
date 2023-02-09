def main():
    meal_time = input("what time is it? ")

    if 7 <= convert(meal_time) <= 8:
        print("breakfast time")
    if 12 <= convert(meal_time) <= 13:
        print("lunch time")
    if 18 <= convert(meal_time) <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    time = float(hours) + float(minutes)/60

    return time

if __name__ == "__main__":
    main()

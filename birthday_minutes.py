import inflect
from datetime import date, timedelta, datetime

def main():
    while True:
        try:
            year, month, day = input("Date of Birth: ").split("/")
            print(delta_dates(year, month, day))
        except ValueError("Invalid date"):
            pass

def delta_dates(year, month, day):

    current_date = date.today()
    birthday = date(int(year), int(month), int(day))

    only_days = sub(current_date, birthday)
    only_days = str(only_days).replace(" days, 0:00:00", "")
    minutes = int(only_days) * 24 * 60
    return convert_numbers(minutes)

def convert_numbers(minutes):
    minute = inflect.engine()
    text = minute.number_to_words(minutes, andword="")
    return f"{text.capitalize()} minutes"

def sub(a, b):
    return a - b
    

if __name__ == '__main__':
    main()
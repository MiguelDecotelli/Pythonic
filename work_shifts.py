import re

# 9 AM to 5 PM
# 9:00 AM to 5:00 PM
# 5:00 PM to 9:00 AM

def main():
    working = convert(input("Hours: "))
    print(str(working))

def convert(s):
    if hours := re.search(r"^([0-1]?[0-9])\:?([0-5][0-9])?\s(AM|PM)\sto\s([0-1]?[1-9])\:?([0-5][0-9])?\s(AM|PM)$", s):
        arrive = hours.group(1)
        leave = hours.group(4)
        arrive_minutes = hours.group(2)
        leave_minutes = hours.group(5)

        if "AM":
            if arrive == "12":
                arrive = "00"

            if leave == "12":
                leave = "00"

        if "PM" in hours.group(3):
            if arrive == "12":
                pass
            else:
                arrive = str(int(arrive) + 12)

        elif "PM" in hours.group(6):
            if leave == "12":
                pass
            else:
                leave = str(int(leave) + 12)
    else:
        raise ValueError

    if arrive_minutes and leave_minutes:
        time = f"{int(arrive):02}:{arrive_minutes} to {int(leave):02}:{leave_minutes}"
    else:
        time = f"{int(arrive):02}:00 to {int(leave):02}:00"
    return time

if __name__ == "__main__":
    main()
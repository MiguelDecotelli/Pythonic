import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))

#255.255.255.255
def validate(ip):
    try:
        bytes = re.match(r"^(\d+)\.+(\d+)\.+(\d+)\.+(\d+)$", ip)
        if int(bytes.group(1)) <= 255 and int(bytes.group(2)) <= 255 and int(bytes.group(3)) <= 255 and int(bytes.group(4)) <= 255:
            return True
        else:
            return False
    except AttributeError:
        return False

if __name__ == "__main__":
    main()
    
import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if you_tube := re.search(r"(?:<iframe)(?:.+)?https?://(?:www\.)?youtube\.com/embed/([a-z0-9]+)",s, re.IGNORECASE):
        return f"https://youtu.be/{you_tube.group(1)}"
    else:
        return None

if __name__ == "__main__":
    main()
def main():
    text = input("Input: ")
    print(f"output: {shorten(text)}")


def shorten(word):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")
        elif letter not in vowels:
            word = word
    return word


if __name__ == "__main__":
    main()
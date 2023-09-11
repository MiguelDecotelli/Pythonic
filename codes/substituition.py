
import sys

def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: ./substitution key\n")

    sub_key = sys.argv[1]

    if not only_letters(sub_key):
        sys.exit("Must use only letters.")

    if len(sub_key) != 26:
        sys.exit("Must contain 26 characters\n")

    if check_duplicates(sub_key):
        sys.exit("Must not contain duplicated characters")

    sub_key = sub_key.lower()

    plaintext = input("Type the plaintext: ")
    print(f"Ciphertext: {encrypting(plaintext, sub_key)} ")


def only_letters(text):
    for i in range(len(text)):
        if not text[i].isalpha():
            return False
    return True


def check_duplicates(text):
    for i in range(len(text)):
        for j in range(i+1, len(text)):
            if text[i].upper() == text[j].upper():
                return True
    return False


def encrypting(text, cipher):
    ciphertext = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_char = ord(char) - 65
                ciphertext += cipher[ascii_char].upper()
            else:
                ascii_char = ord(char) - 97
                ciphertext += cipher[ascii_char]
        else:
            ciphertext += char
    return ciphertext


if __name__ == "__main__":
    main()

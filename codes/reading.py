
def main():
    # Declaring text variable from command-line input.
    text = input("Type your text: ")

    # Declaring varible for letters, words and sentences using respective functions with input text as parameter.
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # Using Coleman-Liau's formula to determine text's grade.
    L = (letters * 100) / words
    S = (sentences * 100) / words
    index = round(0.0588 * L - 0.296 * S - 15.8)

    #  Presenting the different results for every type of text.
    if index < 1:
        print("Text grade is before Grade 1")
    elif index >= 16:
        print("Text grade is 16+")
    else:
        print(f"Text grade is {index}")

def count_letters(text):
    # Declaring and initializing letters variable at 0.
    letters = 0
    # Using a for loop with the length of input text to count for number of letters.
    for i in range(len(text)):
        # Using ISALPHA function, checking if input characters from string are alphabetic letters.
        if text[i].isalpha():
            # Couting letters.
            letters += 1
    # Storing and saving variable for later usage.
    print(f"number of letters is {letters}")
    return letters

# Declaring "count_words" function.

def count_words(text):
    # Using COUNT function to determine if there are spaces between letters to count words. Starting at 1.
    words = text.count(" ") + 1
    # Storing and saving variable for later usage.
    print(f"number of words is {words}")
    return words

# Declaring "count_sentences" function.

def count_sentences(text):
    # Using COUNT function to determine if there are ".", "!" or "?" at the end of words to count for sentences.
    sentences = text.count(".") + text.count("!") + text.count("?")
    # Storing and saving variable for later usage.
    print(f"number of sentences is {sentences}")
    return sentences

if __name__ == "__main__":
    main()
    
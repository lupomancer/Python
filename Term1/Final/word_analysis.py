#! /usr/bin/env python
import os
import re
import sys


def remove_punctuation(passage):
"""This function removes the punctuation from the given file

Arguments:
    passage {string} -- The text file you define in your command line 

Returns:
    string -- The same as the incoming passage but without any punctuation
"""

    punctuation = r"[\W_]+"
    passage = re.sub(punctuation, ' ', passage)
    return passage


def valid_word(chars):
"""Checks if the incoming word is a real word and not numbers or single-character gobbledygook

Arguments:
    chars {string} -- incoming word sent by gen_word_list()

Returns:
    boolean -- Returns a true or false for word validity
"""

    if chars.isalpha():
        if len(chars) > 1 or (len(chars) == 1 and chars in ['a', 'i', 'o']):
            return True
    return False


def gen_word_list(passage):
"""Creates a list of all the words in the incoming passage after removing punctuation and making it lowercase

Arguments:
    passage {string} -- The incoming string from the text file

Returns:
    list -- the list of all the words in the passage
"""

    passage = remove_punctuation(passage)
    passage = passage.lower()
    char_groups = passage.split()
    words = [word for word in char_groups if valid_word(word)]
    words.sort()
    return words


def gen_unique_list(passage):
"""Generates a list off all the uniquie words from the incoming passage after stripping punctuation and passing to lower

Arguments:
    passage {string} -- The incoming passage from the text file

Returns:
    list -- the list of unique words from the passage string
"""

    passage = remove_punctuation(passage)
    passage = passage.lower()
    char_groups = passage.split()
    word_set = {word for word in char_groups if valid_word(word)}
    words = sorted(list(word_set))
    return words


def main():
"""Implements all the functions and prints the final output of gen_word_list() and gen_unique_list()
"""

    # Check if story file is specified on the command line
    if not len(sys.argv) == 2:
        exit(-1)

    # Get current directory of script
    script_dir = os.path.dirname(__file__)

    # Use current directory and story file name to get story file
    with open(os.path.join(script_dir, sys.argv[1])) as news_file:
        # read contents of story file into passage
        passage = news_file.read()

    # generate a list of words in passage
    words = gen_word_list(passage)

    # generate a list of unique words based on raw word list
    unique_words = gen_unique_list(passage)

    # print number of unique words and number of total words
    print("There were {} unique words in the passage out of a total of {} words\n".format(
        len(unique_words), len(words)))

    # print the list of words
    print("Total Words:\n{}".format(words))

    # print the list of unique words
    print("\nUnique Words:\n{}".format(unique_words))


if __name__ == '__main__':
    main()
